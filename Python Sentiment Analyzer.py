import tkinter as tk
from tkinter import ttk

def classify_sentiment(text):
    """
    Classifies the sentiment of a given text using a keyword-based approach.

    This function scores text based on the presence of positive and negative
    keywords. It's a simple but effective method for basic sentiment analysis.

    Args:
        text (str): The input string to be analyzed.

    Returns:
        str: A string indicating the sentiment: 'Positive', 'Negative', or 'Neutral'.
    """
    # Expanded keyword lists for better accuracy
    positive_keywords = [
        'good', 'great', 'awesome', 'excellent', 'love', 'like', 'happy',
        'pleased', 'satisfied', 'wonderful', 'amazing', 'fantastic', 'superb',
        'joy', 'delight', 'breathtaking', 'impressed', 'recommend'
    ]
    negative_keywords = [
        'bad', 'terrible', 'awful', 'horrible', 'hate', 'dislike', 'sad',
        'disappointed', 'unsatisfied', 'poor', 'subpar', 'worst', 'lousy',
        'garbage', 'waste', 'avoid', 'problem'
    ]

    # Convert text to lowercase for case-insensitive matching
    lower_text = text.lower()

    # Score the sentiment based on keyword counts
    positive_score = sum(lower_text.count(word) for word in positive_keywords)
    negative_score = sum(lower_text.count(word) for word in negative_keywords)

    # Classify the sentiment based on the score
    if positive_score > negative_score:
        return 'Positive'
    elif negative_score > positive_score:
        return 'Negative'
    else:
        return 'Neutral'

class SentimentAnalyzerApp:
    """
    A graphical user interface for the Sentiment Analyzer application.

    This class builds a desktop application using tkinter that allows users
    to input text, classify its sentiment, and view a history of their analyses.
    """
    def __init__(self, root):
        """Initializes the application's user interface."""
        self.root = root
        self.root.title("Sentiment Analyzer")

        # Configure the main window aesthetics
        self.root.geometry("600x450")
        self.root.configure(bg='#f0f0f0')

        # Create and configure the main frame with padding
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # --- Input Section ---
        input_label = ttk.Label(main_frame, text="Enter text to analyze:", font=("Helvetica", 12))
        input_label.pack(pady=(0, 10))

        self.text_entry = ttk.Entry(main_frame, width=60, font=("Helvetica", 10))
        self.text_entry.pack(pady=(0, 10), ipady=4)
        # Bind the <Return> key to the analyze_text function for convenience
        self.text_entry.bind("<Return>", self.analyze_text)

        analyze_button = ttk.Button(main_frame, text="Analyze Sentiment", command=self.analyze_text)
        analyze_button.pack(pady=(0, 20))

        # --- Result Section ---
        self.result_label = ttk.Label(main_frame, text="Sentiment: -", font=("Helvetica", 16, "bold"))
        self.result_label.pack()

        # --- History Section ---
        history_frame = ttk.LabelFrame(main_frame, text="Analysis History", padding="10")
        history_frame.pack(fill=tk.BOTH, expand=True, pady=(20, 0))

        # Use a Treeview widget to display history in a structured table
        self.history_tree = ttk.Treeview(history_frame, columns=("Text", "Sentiment"), show="headings")
        self.history_tree.heading("Text", text="Analyzed Text")
        self.history_tree.heading("Sentiment", text="Result")
        self.history_tree.column("Text", width=400)
        self.history_tree.column("Sentiment", width=100, anchor='center')
        self.history_tree.pack(fill=tk.BOTH, expand=True)


    def analyze_text(self, event=None):
        """
        Handles the text analysis event, updates the UI, and logs the history.
        """
        input_text = self.text_entry.get()
        if not input_text.strip():
            # Do nothing if the input is empty
            return

        # Get the sentiment and update the result label with appropriate color
        sentiment = classify_sentiment(input_text)
        self.result_label.config(text=f"Sentiment: {sentiment}", foreground=self.get_sentiment_color(sentiment))

        # Add the new analysis to the top of the history list
        self.history_tree.insert("", 0, values=(input_text, sentiment))

        # Clear the input field for the next analysis
        self.text_entry.delete(0, tk.END)

    def get_sentiment_color(self, sentiment):
        """Returns a distinct color for each sentiment type for better visual feedback."""
        if sentiment == 'Positive':
            return '#2e7d32'  # Dark Green
        elif sentiment == 'Negative':
            return '#c62828'  # Dark Red
        else:
            return '#ff8f00'  # Amber

def main():
    """Sets up the main window and runs the application."""
    root = tk.Tk()
    app = SentimentAnalyzerApp(root)
    root.mainloop()

# Standard entry point for a Python script
if __name__ == "__main__":
    main()