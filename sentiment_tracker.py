import datetime
from textblob import TextBlob
import tkinter as tk
from tkinter import messagebox

def analyze_sentiment(journal_entry):
    # Perform sentiment analysis
    analysis = TextBlob(journal_entry)
    polarity = analysis.sentiment.polarity

    # Classify sentiment
    if polarity > 0:
        return "Positive 😊"
    elif polarity < 0:
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
