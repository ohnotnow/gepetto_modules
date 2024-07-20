import datetime
import argparse
import re
import concurrent.futures
from yaspin import yaspin
from gepetto import bot_factory

def get_llm_thoughts(requirements, bot):
    messages = [
        {
            "role": "system",
            "content": "You are a helpful AI assistant who is an expert at using the Puppet system configuration system.  The user will provide the requirements they need for a module and you need to think through step by step what would be needed, edge cases to consider, best practices, operating system support (the user has to support Rocky Linux, Debian and Ubuntu). You do not need to write the module - your task it to think through the requirements and provide your thoughts so that the user can craft a well written puppet module for their requirements."
        },
        {
            "role": "user",
            "content": f"Hi! I would like your thoughts on what to consider when writing a Puppet module to satisfy the following requirements:\n\n{requirements}"
        }
    ]
    response = bot.chat(messages)
    return response

def create_module(requirements, llm_thoughts, bot):
    messages = [
        {
            "role": "system",
            "content": "You are a helpful AI assistant who is an expert at crafting modules for the Puppet system configuration system.  The user will provide the requirements they need for a module and you need to create a well written, Puppet module with inline comments explaining what it does."
        },
        {
            "role": "user",
            "content": f"Hi! I would like you to create a puppet module for the following requirements:\n\n{requirements}\n\nPlease take into account the following thoughts:\n\n{llm_thoughts}"
        }
    ]
    response = bot.chat(messages)
    return response

def lint_module(module):
    pass

def test_module(module):
    pass

def sanitize_filename(filename):
    filename = filename.replace(" ", "_")
    filename = filename.replace("/", "_")
    filename = filename.replace("\\", "_")
    filename = filename.replace(":", "_")
    filename = filename.replace("*", "_")
    filename = filename.replace("?", "_")
    filename = filename.replace("\"", "_")
    filename = filename.replace("<", "_")
    filename = filename.replace(">", "_")
    filename = filename.replace("|", "_")
    # use a regex to remove and extraneous markdown backticks (possibly with language indicators)
    filename = re.sub(r"```.*\n", "", filename)
    if filename.startswith("."):
        filename = filename[1:]
    if not filename.endswith(".pp"):
        filename = filename + ".pp"
    if not filename:
        filename = "default_module.pp"
    return filename

def create_filename(requirements, bot):
    messages = [
        {
            "role": "system",
            "content": "You are a helpful AI assistant who is an expert with the Puppet system configuration system.  The user will provide you with the requirements they have for a new module, but they have difficulty thinking of a good filename which is Linux filesystem safe.  You should read the requirements and think of a concise filename.  Please resond with only the filename so that the user can copy and paste it easily."
        },
        {
            "role": "user",
            "content": f"Hi! I have the following requirements for a puppet module - but I can't think of a good filename!  Requirements:\n\n{requirements}"
        }
    ]
    response = bot.chat(messages)

    return response

def save_module(module, filename):
    pass

def main(model="gpt-4o-mini", vendor="", requirements_file=""):
    if requirements_file:
        with open(requirements_file, "r") as f:
            requirements = f.read()
    else:
        requirements = input("Enter your requirements:\n")
    start_time = datetime.datetime.now()
    total_cost = 0
    bot = bot_factory.get_bot(model=model, vendor=vendor)

    with yaspin(text="Thinking through requirements...", color="magenta") as spinner:
        llm_thoughts = get_llm_thoughts(requirements, bot)
        total_cost += llm_thoughts.cost
    with yaspin(text="Creating module...", color="cyan") as spinner:
        module = create_module(requirements, llm_thoughts.message, bot)
        total_cost += module.cost
    with yaspin(text="Linting module...", color="yellow") as spinner:
        module_is_valid = lint_module(module.message)
    with yaspin(text="Testing module...", color="green") as spinner:
        test_module(module)
    with yaspin(text="Creating filename...", color="red") as spinner:
        filename = create_filename(requirements, bot)
        total_cost += filename.cost
    with yaspin(text="Saving module...", color="blue") as spinner:
        save_module(module, filename.message)

    end_time = datetime.datetime.now()
    elapsed_time = (end_time - start_time).total_seconds()
    print(f"\n\nTotal time: {round(elapsed_time, 2)} seconds")
    print(f"Total cost: {round(total_cost, 5)}")

if __name__ == "__main__":
    argp = argparse.ArgumentParser()
    argp.add_argument("--requirements-file", type=str, default="", help="A text file containing your requirements")
    argp.add_argument("--model", type=str, default="gpt-4o-mini", help="The LLM model to use")
    argp.add_argument("--vendor", type=str, default="", help="The LLM vendor to use (not needed for openai/anthropic models)")
    args = argp.parse_args()
    main(model=args.model, vendor=args.vendor)
