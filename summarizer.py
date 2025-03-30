from transformers import pipeline

model = "t5-large"
# model = "facebook/bart-large-cnn"

def summarize_text(text):
    summarizer = pipeline("summarization", model=model, truncation=True)
    summary = summarizer(text, max_length=150, min_length=60, truncation=True)
    return summary[0]['summary_text']

def detokenize_text(text, tokenizer):
    tokenized_text = tokenizer.encode(text, add_special_tokens=False)
    decoded_text = tokenizer.decode(tokenized_text, skip_special_tokens=True)
    return decoded_text
