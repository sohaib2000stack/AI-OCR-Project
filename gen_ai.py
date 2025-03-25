from transformers import pipeline
import os

# Load a summarization model (BART is better for summaries)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def read_extracted_text():
    """Reads extracted text from output.txt and ensures fresh data is used."""
    if os.path.exists("output.txt"):
        with open("output.txt", "r", encoding="utf-8") as file:
            return file.read().strip()
    return ""

def generate_text(prompt=None):
    """Summarizes extracted text dynamically based on its length."""

    # If no prompt is provided, read from output.txt
    if not prompt:
        prompt = read_extracted_text()

    # Prevent AI from processing empty or very short text
    if not prompt or len(prompt.split()) < 10:
        return "⚠️ The extracted text is too short for AI processing."

    # Calculate dynamic max_length (half of input tokens, but at least 50)
    input_length = len(prompt.split())
    max_length = max(input_length // 2, 50)  # Ensure a minimum summary length of 50
    min_length = max(max_length // 3, 30)  # Ensures summary isn't too short

    # If the text is too long, split it into smaller chunks and summarize each
    if input_length > 1024:
        chunks = [prompt[i:i + 1024] for i in range(0, len(prompt), 1024)]
        summaries = []
        
        for chunk in chunks:
            summary = summarizer(chunk, max_length=max(len(chunk.split()) // 2, 50), min_length=min_length, do_sample=False)
            summaries.append(summary[0]["summary_text"])

        return " ".join(summaries)

    # Otherwise, summarize normally
    summary = summarizer(prompt, max_length=max_length, min_length=min_length, do_sample=False)

    return summary[0]["summary_text"]




















































