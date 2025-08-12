A simple desktop application built with Python and Tkinter that analyzes text and classifies its sentiment as Positive, Negative, or Neutral.

This project serves as a great introduction to GUI development with Tkinter and basic Natural Language Processing (NLP) concepts.


Features
Simple & Clean UI: An intuitive and easy-to-use graphical interface.

Real-time Analysis: Instantly classify the sentiment of any text you enter.

Analysis History: View a log of your previous analyses in a clear, table-based format.

Keyword-Based Logic: Uses a straightforward and easy-to-understand algorithm based on positive and negative keywords.

Cross-Platform: Built with Python's standard Tkinter library, it should run on Windows, macOS, and Linux without issues.


How It Works
The sentiment analysis logic is intentionally simple. The core classify_sentiment function works as follows:

Keyword Lists: It maintains two lists of words: one for positive sentiment (e.g., "good", "great", "amazing") and one for negative sentiment (e.g., "bad", "terrible", "awful").

Text Scoring: It converts the input text to lowercase and counts the occurrences of each positive and negative keyword.


Classification:

If the positive keyword count is higher, the sentiment is classified as Positive.

If the negative keyword count is higher, it's classified as Negative.

If the counts are equal (including both being zero), it's classified as Neutral.


Installation and Usage
No external libraries are required to run this application, as it only uses Python's built-in tkinter module.


Prerequisites:

Make sure you have Python 3 installed on your system.

Tkinter is usually included with Python installations. If not, you may need to install it separately (e.g., sudo apt-get install python3-tk on Debian/Ubuntu).

Clone the repository:

git clone https://github.com/Runasth/Python_Sentiment_Analyzer.git
cd Python_Sentiment_Analyzer

Run the application:

python sentiment_analyzer.py


Contributing
Contributions are welcome! If you have ideas for improvements or want to fix a bug, please feel free to fork the repository and submit a pull request.

Possible areas for contribution include:

Improving the keyword lists.

Implementing a more advanced NLP model (e.g., using NLTK, spaCy, or a pre-trained model).

Adding data visualization for the analysis history.

Refining the UI/UX.


License
This project is licensed under the MIT License. See the LICENSE file for more details
