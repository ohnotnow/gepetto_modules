# Common LLM Interface Modules

This repository contains a set of common Python modules designed to facilitate interaction with various large language models (LLMs) through a unified interface. By abstracting the complexities of different models, these modules enable developers to integrate LLM capabilities into their projects more efficiently.

## Example

The included `main.py` script demonstrates how to use the common interface to interact with an LLM, specifically the `gpt-4o` model. The example sends a simple chat message and prints the response.

```python
import datetime
import argparse
import concurrent.futures
from yaspin import yaspin
from gepetto import bot_factory

def main():
    start_time = datetime.datetime.now()
    total_cost = 0
    model = "gpt-4o"
    bot = bot_factory.get_bot(model=model)
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "How do I make soup?"
        }
    ]
    response = bot.chat(messages) # use the default model
    response = bot.chat(messages, model="gpt-4o-mini") # override the model for this call
    print(response)
    # with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    #     costs = executor.map(process_file, file_list, [a11y]*len(file_list), [responsive]*len(file_list), [css]*len(file_list), [model]*len(file_list))

    # total_cost = sum(costs)
    end_time = datetime.datetime.now()
    elapsed_time = (end_time - start_time).total_seconds()
    print(f"\n\nTotal time: {round(elapsed_time, 2)} seconds")
    print(f"Total cost: {round(total_cost, 5)}")

if __name__ == "__main__":
    argp = argparse.ArgumentParser()
    argp.add_argument("--example", type=str, default="", help="An option")
    args = argp.parse_args()
    main()
```

## Installation

To use the modules in this repository, follow the installation instructions below based on your operating system.

### MacOS and Ubuntu

1. **Clone the repository:**
    ```bash
    git clone https://github.com/ohnotnow/gepetto_modules
    cd gepetto_modules
    ```

2. **Set up a virtual environment and install dependencies:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

### Windows

1. **Clone the repository:**
    ```bash
    git clone https://github.com/ohnotnow/gepetto_modules
    cd gepetto_modules
    ```

2. **Set up a virtual environment and install dependencies:**
    ```bash
    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt
    ```

## Running the Code

To run the example script, use the following command:
```bash
python main.py
```

You can also provide an optional argument:
```bash
python main.py --example <value>
```

Replace `<value>` with your specific input.

## License

This project is licensed under the MIT License.
