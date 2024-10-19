import google.generativeai as genai
import subprocess
import shlex
import os

# replace with your actual api key
api_key = "API KEY"
if not api_key:
    raise ValueError("API key not found, make sure to add api key on the code or you can create environment var if secuirty is needed.")

# Configure the generative AI API usig api key
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash") #AI MODEL , can be changed if needed

def is_safe_command(command):
    """Check if the command is safe to execute on Windows."""
    disallowed_commands = []  # Add disallowed commands if needed such as shutdown commands, deleting commands and many more risky cmds
    return not any(command.lower().startswith(disallowed) for disallowed in disallowed_commands)

def clean_command(command):
    """Clean up the command by stripping extra formatting like code blocks."""
    command = command.strip()
    if command.startswith("```"):
        command = command[3:-3].strip()  # Remove markdown code block markers
    return command

while True:
    prompt = input("YOU> ").strip()  # Get user input
    if prompt.lower() in ['exit', 'quit']:
        print("Exiting the script.")
        break

    try:
        # Generate a command from the model based on the user's prompt, here the pompting plays important role in this code because ai can generate useless text which results in error to make it only generate the commandf bteer pompting is needed
        response = model.generate_content(
            f"You have full access to my Windows system. Only provide the exact shell command needed for the task, "
            f"using commands that work in Windows Command Prompt (cmd.exe). Ensure correct file paths using '\\' and "
            f"avoid Linux/Unix commands like 'ls' or 'rm'. Do not include explanations, comments, or greetings. "
            f"Failure to comply will result in an error. Generate a shell command for this task: {prompt}."
        )
    except Exception as e:
        print(f"Error generating command: {e}")
        continue

    if response and response.text:
        command = response.text.strip()

        # Clean and validate the command
        cleaned_command = clean_command(command)
        print(f"Cleaned Command: '{cleaned_command}'")

        if is_safe_command(cleaned_command):
            try:
                # Execute the cleaned command
                result = subprocess.run(
                    shlex.split(cleaned_command), check=True, capture_output=True, text=True, shell=True
                )
                print("Command Output:\n", result.stdout)
            except subprocess.CalledProcessError as e:
                print(f"Error executing command: {e.stderr}")
            except Exception as ex:
                print(f"Unexpected error: {ex}")
        else:
            print("Command execution aborted due to safety concerns.")
    else:
        print("No valid command generated. Please try again.")
