from textblob import TextBlob

# Perform sentiment analysis on a text
text = "Bitcoin is experiencing a bullish rally!"
text1= "Textblob is amazingly simple to use. What great fun!"
blob = TextBlob(text1)
sentiment = blob.sentiment

# Print the sentiment polarity and subjectivity
print(sentiment.polarity)
print(sentiment.subjectivity)