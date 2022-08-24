from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarizeText(text, max_length=130):
    summaries = summarizer(text, max_length=max_length, min_length=30, do_sample=False)
    firstSummary = summaries[0]
    return firstSummary['summary_text']

