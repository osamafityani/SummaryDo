import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from flask import Flask, request, jsonify, after_this_request
from heapq import nlargest

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

    maxFrequency = max(wordFrequencies.values())
    for key in wordFrequencies.keys():
        wordFrequencies[key] = wordFrequencies[key] / maxFrequency

    sentenceTokens = [sent for sent in doc.sents]

    sentenceScores = {}

    for sent in sentenceTokens:
        for word in sent:
            wordLower = word.text.lower()
            if wordLower in wordFrequencies.keys():
                if wordLower not in sentenceScores:
                    sentenceScores[sent] = wordFrequencies[wordLower]
                else:
                    sentenceScores[sent] += wordFrequencies[wordLower]
    selectRange = int(len(sentenceTokens) * 0.3)
    summarySentences = nlargest(selectRange, sentenceScores, sentenceScores.get)

    summary = []
    for sent2 in sentenceTokens:
        for sent1 in summarySentences:
            if sent1 == sent2:
                summary.append(sent1)

    summary = [word.text for word in summary]

    summary = ' '.join(summary)

    return summary

app = Flask(__name__)


@app.route('/', methods=['POST'])
def upload_data():
    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    data = request.get_json(force=True)
    return jsonify(textSummarize(data['dscr']))


if __name__ == '__main__':
    app.run(host='localhost', port=8989)
