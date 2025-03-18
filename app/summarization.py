from transformers import pipeline

# Load summarization model
summarization_models = {
    "bart": pipeline("summarization", model="facebook/bart-large-cnn"),
    "t5": pipeline("summarization", model="t5-small"),
    "pegasus": pipeline("summarization", model="google/pegasus-xsum")
}

def trim_summary_to_100_words(summary):
    """Trims a summary to be within 100 words while maintaining coherence."""
    words = summary.split()
    if len(words) > 100:
        return " ".join(words[:100]) + "..."
    return summary

def summarize_large_text(text, model="bart"):
    """Summarizes text and ensures the summary does not exceed 100 words."""
    summarizer = summarization_models.get(model, summarization_models["bart"])

    # Generate summary
    raw_summary = summarizer(text, max_length=200, min_length=50, do_sample=False)[0]["summary_text"]

    # Trim to 100 words
    return trim_summary_to_100_words(raw_summary)
