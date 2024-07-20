# Project: Puppet Module Generator

## Description
The Puppet Module Generator is a command-line tool designed to help users create Puppet modules based on given requirements. It leverages a language model to think through the requirements, generate the module, and suggest a filename, ensuring that the module adheres to best practices and is compatible with Rocky Linux, Debian, and Ubuntu.

## Features
- Analyzes and processes user-provided requirements.
- Generates Puppet modules with inline comments.
- Lints and tests the generated module.
- Suggests and sanitizes filenames for the module.
- Tracks the total cost and time taken for the module generation process.

## Installation

### Requirements
- Python 3.6+
- `pip` (Python package installer)
- A supported LLM model

### Installation Steps

1. **Clone the repository**
    ```sh
    git clone https://github.com/ohnotnow/puppet_creator
    cd puppet_creator
    ```

2. **Set up a virtual environment and install dependencies**

    #### On MacOS and Ubuntu:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

    #### On Windows:
    ```sh
    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt
    ```

## Usage

Run the script using the command line. You can provide a file containing your requirements or enter them manually.

### Command-Line Arguments

- `--requirements-file`: Path to a text file containing the module requirements.
- `--model`: The LLM model to use (default: `gpt-4o-mini`).
- `--vendor`: The LLM vendor to use (not needed for openai/anthropic models).

### Example Usage

#### Using a requirements file:
```sh
python main.py --requirements-file path/to/module_requirements.txt
```

#### Entering requirements manually:
```sh
python main.py
```

#### Using different models:
You can use different models and API providers if you like.  You will need to set the appropriate environment variables to access them, for instance :
```sh
export OPENAI_API_KEY=...
export ANTHROPIC_API_KEY=...
export ANYSCALE_API_KEY=...
export GROQ_API_KEY=....
```
And then:
```sh
python main.py --model=claude-3-5-sonnet-20240620
python main.py --model=llama3-70b-8192 --vendor=groq
```

## Detailed Steps

1. **Read Requirements**: Reads the requirements either from a file or manual input.
2. **Think Through Requirements**: Uses the language model to analyze and provide thoughts on the requirements.
3. **Create Module**: Generates a Puppet module based on the requirements and the model's thoughts.
4. **Lint Module**: Ensures the generated module adheres to best practices.
5. **Test Module**: Runs tests on the generated module to ensure functionality.
6. **Create Filename**: Suggests a Linux filesystem-safe filename for the module.
7. **Save Module**: Saves the module with the generated filename.

## License
MIT License
