from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your actual API key from a translation service provider
API_KEY = 'YOUR_API_KEY'
TRANSLATE_URL = "https://translation.googleapis.com/language/translate/v2"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    text = request.form['text']
    source_lang = request.form['source_lang']
    target_lang = request.form['target_lang']
    
    params = {
        'q': text,
        'source': source_lang,
        'target': target_lang,
        'key': API_KEY
    }
    response = requests.post(TRANSLATE_URL, data=params)
    translation = response.json().get('data').get('translations')[0].get('translatedText')
    
    return jsonify({'translation': translation})

if __name__ == "__main__":
    app.run(debug=True)
