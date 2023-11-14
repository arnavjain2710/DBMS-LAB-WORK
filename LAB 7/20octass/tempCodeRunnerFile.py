from flask import Flask, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

app = Flask(__name__)

clf = joblib.load('spam_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        email_text = request.form['email_text']
        prediction = detect_spam(email_text)
        result = "Spam" if prediction == 1 else "Not Spam"
    return render_template('index.html', result=result)

def detect_spam(email_text):
    email_text = [email_text]
    X_test = vectorizer.transform(email_text)
    prediction = clf.predict(X_test)

    return prediction[0]

if __name__ == '__main__':
    app.run(debug=True)
