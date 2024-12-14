**Sentiment Analysis App**

This is a web application that analyzes the sentiment of a given text or paragraph using TextBlob, a Python library for processing textual data. The app allows users to enter a paragraph and see the sentiment analysis result.

---

**Getting Started**

1. Clone the repository and Set up the environment
Clone the repository to your local machine and navigate to the project directory:

>>>git clone https://github.com/yourusername/sentiment_analyzer.git
>>>cd sentiment_analyzer

2. Set up a virtual environment to isolate dependencies. If you haven't already installed virtualenv, you can do so using pip. Then create and activate the virtual environment:

---Install virtualenv
>>>  pip install virtualenv

---# On Windows
>>   python -m venv venv
>>   .\venv\Scripts\activate

---# On macOS/Linux
>>   python3 -m venv venv
>> source venv/bin/activate# On macOS/Linux

3. Install the necessary dependencies or create a requirements.txt file:

Install dependencies
>> pip install django textblob nltk matplotlib

Optional: Create a requirements.txt

>> echo "django==4.1.0" >> requirements.txt
>> echo "textblob==0.15.3" >> requirements.txt
>> echo "nltk==3.6.3" >> requirements.txt
>> echo "matplotlib==3.4.3" >> requirements.txt

Download the necessary NLTK corpora for sentence tokenization to avoid errors:

>> import nltk
>> nltk.download('punkt')

4. Finally, run the Django development server to launch the app:

>> python manage.py runserver
The application should now be accessible at http://127.0.0.1:8000/.

**How to Use**

Open the web app in your browser.
--Enter a paragraph of text in the input field.
--Click the "Analyze" button to see the sentiment result.
--The sentiment polarity (positive/negative) and subjectivity (objective/subjective) will be displayed.
--A graphical plot will be shown based on the sentiment analysis.

Troubleshooting
If you encounter the following error while running the app:

MissingCorpusError: Looks like you are missing some required data for this feature.

Follow these steps by opening a Python shell:

>> import nltk
>> nltk.download('punkt')
