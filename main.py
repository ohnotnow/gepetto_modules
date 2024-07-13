import datetime
import argparse
import concurrent.futures
from yaspin import yaspin
from gepetto import bot_factory


def main(model="gpt-4o", vendor=""):
    start_time = datetime.datetime.now()
    total_cost = 0
    bot = bot_factory.get_bot(model=model, vendor=vendor)
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
    response = bot.chat(messages, model=model)
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
    argp.add_argument("--model", type=str, default="gpt-4o", help="The LLM model to use")
    argp.add_argument("--vendor", type=str, default="", help="The LLM vendor to use (not needed for openai/anthropic models)")
    args = argp.parse_args()
    main(model=args.model, vendor=args.vendor)
