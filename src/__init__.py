from flask import Flask, request, render_template, redirect, url_for
import joblib

app = Flask(__name__)


def sentiment_analysis(sentence):
    model = joblib.load('models/saved_model')
    vectorizer = joblib.load('models/saved_vectorizer')

    v = vectorizer.transform(sentence)
    sentiment = model.predict(v)[0]

    if sentiment == 0:
        return 'neutral'
    if sentiment > 0:
        return 'positive'
    if sentiment < 0:
        return 'negative'


@app.route('/home')
def home():
    sentiment = request.args.get('sentiment')

    return render_template('home.html', sentiment=sentiment)


@app.route('/api/v1/sentiment-analyzer', methods=['POST'])
def sentiment_analyzer():
    sentence = request.form['sentence']
    sentiment = sentiment_analysis([sentence])

    return redirect(url_for('home', sentiment=sentiment))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
