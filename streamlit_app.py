import streamlit as st
from textblob import TextBlob

st.title("Sentiment Analyzer")
text = st.text_area("Enter text to analyze:")

if st.button("Analyze"):
    if text:
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        if polarity > 0:
            sentiment = "Positive"
        elif polarity < 0:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"
        st.success(f"Sentiment: {sentiment}")
    else:
        st.warning("Please enter some text.")
