# Personal Journal Sentiment Tracker

**Personal Journal Sentiment Tracker** is a Python application that combines journaling with sentiment analysis. It helps you track your journal entries while analyzing and categorizing the sentiment of each entry as Positive, Negative, or Neutral.

## Features

- **Sentiment Analysis:** Uses the [TextBlob](https://textblob.readthedocs.io/en/dev/) library to determine the sentiment polarity of journal entries.
- **Interactive CLI Mode:** Write journal entries directly in the console.
- **GUI Mode:** A simple graphical user interface for writing entries and displaying sentiment.
- **Persistent Storage:** Saves your journal entries along with their sentiment to a text file (`journal_entries.txt`).

## File Structure

- `sentiment_tracker.py`: The main script containing the functionality for both CLI and GUI modes.

## Requirements

- Python 3.6 or later
- Required Python libraries:
  - `textblob`
  - `tkinter` (comes pre-installed with Python)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Molidier/personal-journal-sentiment-tracker.git
   cd personal-journal-sentiment-tracker
   ```

2. Install dependencies:

   ```bash
   pip install textblob
   ```

3. (Optional) Download and install the NLTK corpora for TextBlob:

   ```bash
   python -m textblob.download_corpora
   ```

## Usage

### CLI Mode

1. Run the script:

   ```bash
   python sentiment_tracker.py
   ```

2. Follow the prompts to write your journal entries. Type `exit` to quit.

### GUI Mode

1. Run the script:

   ```bash
   python sentiment_tracker.py
   ```

2. A graphical window will appear:
   - Write your journal entry in the text box.
   - Click **Analyze Sentiment** to see the sentiment of your entry.

## Example

### CLI Example:

```plaintext
Welcome to your Personal Journal Sentiment Tracker!

Write your journal entry (or type 'exit' to quit): I had a fantastic day!
Sentiment Analysis: Positive 😊

Write your journal entry (or type 'exit' to quit): It's been a tough week.
Sentiment Analysis: Negative 😢
```

### GUI Example:

1. Enter your journal entry in the text box.
2. Click **Analyze Sentiment**.
3. The sentiment (e.g., "Positive 😊") will appear below the button.

## Output

Entries are saved in `journal_entries.txt` in the format:

```plaintext
YYYY-MM-DD | Journal Entry | Sentiment
```

Example:

```plaintext
2025-01-12 | I had a fantastic day! | Positive 😊
2025-01-13 | It's been a tough week. | Negative 😢
```
