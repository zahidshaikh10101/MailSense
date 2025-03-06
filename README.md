# Mailsense - Smarter Insights, Safer Inbox, Seamless Replies!

**Mailsense** is a powerful web application that provides users with smarter insights into their emails, helping to manage their inbox more effectively. This application combines advanced machine learning models and natural language processing (NLP) techniques to offer four main functionalities: **Spam/Ham Classification**, **Sentiment Analysis**, **Email Summarization**, and **Auto-Reply Generation**.

With **Mailsense**, users can:
- Classify emails as **Spam** or **Ham** using a trained Multinomial Naive Bayes model.
- Analyze the **Sentiment** of the email to determine if it's **Positive**, **Negative**, or **Neutral**.
- Get a **Summary** of the email content for quick understanding.
- Receive **Auto-Generated Replies** for easy email responses.

---

## Features

### 1. **Spam/Ham Classification**
- **Description**: Classify emails as either **Spam** or **Ham** (legitimate) using a **Multinomial Naive Bayes** model.
- **How to use**:
  - Paste the email or email chain into the textarea.
  - Click **Analyze** to see whether the email is **Spam** or **Ham**.

### 2. **Sentiment Analysis**
- **Description**: Determine the sentiment of the email using the **SentimentIntensityAnalyzer** from **NLTK**’s **vader_lexicon**.
- **How it works**:
  - Analyzes the tone of the email and classifies it as **Positive**, **Negative**, or **Neutral**.

### 3. **Email Summarizer**
- **Description**: Generates a brief summary of the email or email chain to help you understand the key points quickly.
- **How to use**:
  - Paste the email into the textarea.
  - Click **Analyze** to receive a summarized version of the email.

### 4. **Auto-Reply Generator**
- **Description**: Generates 3 possible responses to the email that you can easily copy and paste as a reply.
- **How to use**:
  - Paste the email into the textarea.
  - Click **Analyze** to receive 3 suggested replies to the email.

---

## Installation & Usage

Follow the steps below to set up and run **Mailsense** on your local machine.

### 1. Clone the repository:
```bash
git clone https://github.com/zahidshaikh10101/Mailsense.git
```
2. Navigate to the project directory:
   ```bash
   cd Mailsense
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python app.py
   ```
5. Open your browser and go to:
   ```
   [http://localhost:8000](http://127.0.0.1:5000/)
   ```

---


## Screenshots
<img width="557" alt="app" src="https://github.com/zahidshaikh10101/MailSense/blob/main/images/0.png"> 
<img width="557" alt="app" src="https://github.com/zahidshaikh10101/MailSense/blob/main/images/1.png"> 
<img width="557" alt="app" src="https://github.com/zahidshaikh10101/MailSense/blob/main/images/2.png"> 
<img width="557" alt="app" src="https://github.com/zahidshaikh10101/MailSense/blob/main/images/3.png"> 
<img width="557" alt="app" src="https://github.com/zahidshaikh10101/MailSense/blob/main/images/4.png"> 


---

## Technologies Used
- **Python** (Streamlit, Pandas, ReportLab, Requests, Tqdm, Regular Expressions (re), io, os, time, datetime, json)
- **APIs** (YouTube Media Downloader, YouTube Transcript API, Google Generative AI (Gemini))

- **Python**
- **Machine Learning:**
  - Multinomial Naive Bayes for Spam/Ham Classification.
  - SentimentIntensityAnalyzer (NLTK's vader_lexicon) for sentiment analysis.
  - Google Generative AI (Gemini) for summarizing emails and generating auto-replies.
- **Libraries:**
  - Flask for web framework.
  - Pickle for loading machine learning models.
  - NLTK for natural language processing tasks like sentiment analysis.
  - google-generativeai for email summarization and auto-replies.
    
---

## Contribution
If you’d like to contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Commit your changes.
4. Push to the branch and submit a Pull Request.

---

## Contact
For any queries or suggestions, feel free to reach out:
- **Email**: zahidshaikh10101@gmail.com
- **GitHub**: [zahidshaikh10101](https://github.com/zahidshaikh10101)

---

### Enjoy using VidSage! 🎥📌📥



