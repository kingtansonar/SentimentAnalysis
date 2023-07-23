
from textblob import TextBlob
# Example text
text = input("enter the text ")

# Create a TextBlob object
blob = TextBlob(text)

# Perform sentiment analysis
sentiment = blob.sentiment.polarity

# Print the sentiment score
if sentiment > 0:
    print("Positive sentiment")
elif sentiment < 0:
    print("Negative sentiment")
else:
    print("Neutral sentiment")
