from flask import Flask, render_template, request
import pickle
import os
import google.generativeai as genai
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')

app = Flask(__name__)

model = pickle.load(open('multinomial_naive_bayes.pkl','rb'))
feature_extraction = pickle.load(open('feature_extraction.pkl','rb'))

sia = SentimentIntensityAnalyzer()
def analyze_sentiment(email_text):
    sentiment_score = sia.polarity_scores(email_text)["compound"]
    if sentiment_score >= 0.05:
        return "Positive"
    elif sentiment_score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

def email_summarizer(emails):
    genai.configure(api_key="") # Add your API KEY
    generation_config = {
    "temperature": 0.7,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 5000,
    "response_mime_type": "text/plain",
    }
    prompt = f'''
    Please Summarize the email/email chains {emails} in brief
    '''
    model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-thinking-exp-01-21",
    generation_config=generation_config,
    )
    chat_session = model.start_chat(
    history=[
    ]
    )
    response = chat_session.send_message(prompt)
    return response.text

def email_replyer(emails):
    genai.configure(api_key="") # Add your API KEY
    generation_config = {
    "temperature": 0.7,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 5000,
    "response_mime_type": "text/plain",
    }
    prompt = f'''
    Please write appropriate reply to the email/email chains {emails} in less then 300 words
    '''
    model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-thinking-exp-01-21",
    generation_config=generation_config,
    )
    chat_session = model.start_chat(
    history=[
    ]
    )
    response = chat_session.send_message(prompt)
    return response.text


def predict_mail(input_text):
    input_user_mail = [input_text]
    input_data_features = feature_extraction.transform(input_user_mail)
    prediction = model.predict(input_data_features)
    return prediction

@app.route('/', methods=['GET', 'POST'])
def analyze_mail():
    if request.method == 'POST':
        mail = request.form.get('mail')  # Get user email input

        if not mail.strip():  # Ensure mail is not empty
            return render_template('index.html', error="Email content cannot be empty.")
        
        # Predict spam or ham
        predicted_mail = predict_mail(input_text=mail)

        # Analyze sentiment
        sentiment = analyze_sentiment(mail)

        # Summarizer
        summarizer = email_summarizer(mail)

        # Replyer
        replyer = email_replyer(mail)

        return render_template('index.html', classify=predicted_mail, mail=mail, sentiment=sentiment, summarizer=summarizer, replyer=replyer)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
