from gepetto import anyscale, gpt, ollama, groq, claude

def get_bot(model="gpt-4o", vendor="unknown"):
    if model.startswith('gpt'):
        bot = gpt.GPTModelSync()
    elif model.startswith('claude'):
        bot = claude.ClaudeModelSync()
    elif vendor.startswith('ollama'):
        bot = ollama.OllamaModelSync()
    elif vendor.startswith('groq'):
        bot = groq.GroqModelSync()
    elif vendor.startswith('anyscale'):
        bot = anyscale.MistralModelSync()
    else:
        raise ValueError(f"Cannot find a bot for : {model} / {vendor}")
    return bot
