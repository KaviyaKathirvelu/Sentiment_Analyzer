import os
import matplotlib
matplotlib.use('Agg')
from django.shortcuts import render
from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import nltk

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')


def home(request):
    overall_sentiment = None
    detailed_sentiments = []  # To store sentence-by-sentence sentiment analysis
    message = None
    wordcloud_image = None  # To store the word cloud image

    if request.method == "POST":
        text = request.POST.get('text', '').strip()
        if text:
            # Generate Word Cloud
            wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

            # Convert Word Cloud to an image and encode it
            plt.figure(figsize=(8, 4))
            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis('off')
            buffer = BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            wordcloud_image = base64.b64encode(buffer.getvalue()).decode('utf-8')
            buffer.close()

            # Sentiment Analysis for the entire text
            blob = TextBlob(text)
            polarity = blob.sentiment.polarity
            if polarity > 0:
                overall_sentiment = "Positive"
            elif polarity < 0:
                overall_sentiment = "Negative"
            else:
                overall_sentiment = "Neutral"

            # Sentence-by-sentence Sentiment Analysis
            sentences = blob.sentences
            for sentence in sentences:
                sentence_text = str(sentence)
                sentence_polarity = sentence.sentiment.polarity
                if sentence_polarity > 0:
                    sentiment = "Positive"
                elif sentence_polarity < 0:
                    sentiment = "Negative"
                else:
                    sentiment = "Neutral"
                detailed_sentiments.append({'sentence': sentence_text, 'sentiment': sentiment})

        else:
            message = "Please enter some text to analyze."

    return render(request, 'sentiment_app/home.html', {
        'overall_sentiment': overall_sentiment,
        'detailed_sentiments': detailed_sentiments,
        'message': message,
        'wordcloud_image': wordcloud_image
    })
