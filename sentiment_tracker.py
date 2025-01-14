import datetime
import tkinter as tk
from tkinter import messagebox
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# Ensure VADER is available
nltk.download("vader_lexicon")

# Initialize SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

def analyze_sentiment(journal_entry):
    # Perform sentiment analysis
    sentiment_scores = sia.polarity_scores(journal_entry)
    compound_score = sentiment_scores["compound"]

    # Classify sentiment
    if compound_score > 0.05:
        return "Positive 😊"
    elif compound_score < -0.05:
        return "Negative 😢"
    else:
        return "Neutral 😐"

def journal_tracker():
    print("Welcome to your Personal Journal Sentiment Tracker!")
    while True:
        # Get journal entry
        entry = input("\nWrite your journal entry (or type 'exit' to quit): ")
        if entry.lower() == 'exit':
            print("Goodbye!")
            break

        # Analyze sentiment
        sentiment = analyze_sentiment(entry)
        print(f"Sentiment Analysis: {sentiment}")

        # Optional: Save entry and sentiment to a file
        with open("journal_entries.txt", "a") as file:
            date = datetime.date.today().strftime("%Y-%m-%d")
            file.write(f"{date} | {entry} | {sentiment}\n")

def analyze_and_display():
    entry = text_box.get("1.0", "end-1c")  # Get user input from text box
    if not entry.strip():
        messagebox.showwarning("Empty Entry", "Please write something!")
        return
    
    sentiment = analyze_sentiment(entry)
    result_label.config(text=f"Sentiment: {sentiment}")

# Set up GUI
root = tk.Tk()
root.title("Journal Sentiment Tracker")

tk.Label(root, text="Write your journal entry:").pack()
text_box = tk.Text(root, height=10, width=50)
text_box.pack()

analyze_button = tk.Button(root, text="Analyze Sentiment", command=analyze_and_display)
analyze_button.pack()

result_label = tk.Label(root, text="Sentiment: ", font=("Arial", 14))
result_label.pack()

root.mainloop()
