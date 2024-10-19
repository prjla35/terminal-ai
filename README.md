# Windows Command Executor with Google Generative AI

This project integrates Google Generative AI to generate and execute Windows Command Prompt commands based on natural language user input. The script allows you to describe tasks in plain English, and the AI generates the appropriate Windows shell command.

## Features

- **Natural Language Input**: Users can provide prompts, and the AI generates Windows-compatible commands.
- **Windows-Specific Commands**: The model is fine-tuned to ensure commands work with Windows Command Prompt.
- **Safety Checks**: Commands are validated for safety before execution.
- **Command Execution**: Valid commands are run on your Windows machine, with output displayed in the terminal.

## Prerequisites

- Python 3.x
- A Google Cloud account with access to the [Google Generative AI API](https://cloud.google.com/generative-ai).
- An API key from Google Generative AI.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/prjla35/terminal-ai
    cd terminal-ai
    ```

2. **Install required dependencies**:
    ```bash
    pip install google-generativeai
    ```

3. **Set up your Google API Key**:

    - Obtain an API key from Google Generative AI.
    - Add the API key to your environment variable or directly modify the `api_key` variable in the script.

4. **Run the script**:
    ```bash
    python command_executor.py
    ```

## Usage

1. **Start the script**:
    ```bash
    python command_executor.py
    ```

2. **Input natural language prompts**:  
    For example:
    ```
    YOU> Show me the contents of the C:\Users folder.
    ```

3. **Command Execution**:  
    The AI will generate a Windows command based on your input and run it. Output will be shown in the terminal.

4. **Exit the script**:  
    Type `exit` or `quit` to terminate the program.


## AI Assistance and Accuracy Limitations

**Note**: This code was created with significant help from AI. While the initial logic and structure were provided by the AI, the final implementation and adjustments were made manually. Using AI accelerated the development process and provided useful insights.

However, due to the limitations and potential inaccuracies of Google Gemini (and other large language models), the AI may occasionally generate incorrect commands or fail to execute a task properly. In such cases, consider using alternative LLMs, such as OpenAI’s ChatGPT, for more accurate results or as a fallback when you encounter errors.

## Safety

This script includes safety checks. While currently no commands are restricted, you can customize the `is_safe_command` function by adding any commands you wish to block.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

1. Fork the repository.
2. Create a new feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push the branch: `git push origin feature/your-feature`
5. Open a pull request.
