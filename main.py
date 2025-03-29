import click
from transformers import pipeline, AutoTokenizer
from dotenv import load_dotenv
import os
load_dotenv()
token = os.getenv("HUGGINGFACE_TOKEN")

# model = "facebook/bart-large-cnn"
model = "t5-large"

def summarize_text(text):
    summarizer = pipeline("summarization", model=model, truncation=True)
    summary = summarizer(text, max_length=150, min_length=60, truncation=True)
    return summary[0]['summary_text']

def detokenize_text(text, tokenizer):
    tokenized_text = tokenizer.encode(text, add_special_tokens=False)
    decoded_text = tokenizer.decode(tokenized_text, skip_special_tokens=True)
    return decoded_text

@click.command()
@click.argument('input_text')
def main(input_text):
    tokenizer = AutoTokenizer.from_pretrained(model)
    summary = summarize_text(input_text)
    cleaned_summary = detokenize_text(summary, tokenizer)
    print("Summary:", cleaned_summary)

if __name__ == "__main__":
    main()
