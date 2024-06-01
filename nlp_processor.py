from langdetect import detect
from transformers import AutoTokenizer

def detect_language(text):
    lang = detect(text)
    if lang in ['es', 'ca', 'en']:
        return lang
    else:
        return None

def preprocess_text(text, lang):
    tokenizer = AutoTokenizer.from_pretrained(f"bert-base-{lang}-cased")
    tokens = tokenizer.tokenize(text)
    return tokenizer.convert_tokens_to_ids(tokens)

