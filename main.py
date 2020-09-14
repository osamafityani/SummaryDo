import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from flask import Flask, request, jsonify, after_this_request

stopWords = list(STOP_WORDS)
nlp = spacy.load('en_core_web_sm')


def textSummarize(text):
    doc = nlp(text)

    tokens = [token for token in doc]

    wordFrequencies = {}

    for word in tokens:
        wordLower = word.text.lower()
        if (wordLower not in stopWords) and (wordLower not in punctuation):
            if wordLower not in wordFrequencies.keys():
                wordFrequencies[wordLower] = 1
            else:
                wordFrequencies[wordLower] += 1
    return wordFrequencies

app = Flask(__name__)


@app.route('/', methods=['POST'])
def upload_data():
    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    data = request.get_json()
    print(data['dscr'])
    return jsonify(textSummarize(data['dscr']))


if __name__ == '__main__':
    app.run(host='localhost', port=8989)






