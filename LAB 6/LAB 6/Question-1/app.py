from flask import Flask, render_template, request
from sentiment_analysis import analyze_sentiment

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text']
    sentiment = analyze_sentiment(text)
    return render_template('result.html', sentiment=sentiment)

if __name__ == '__main__':
    app.run(debug=True)

