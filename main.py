import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation

text = """
"Solids: 100% Cotton; Sport Grey: 90% Cotton, 10% Polyester
Imported
Machine wash
Solids: 100 percent cotton; Sport grey: 90 percent cotton, 10 percent polyester
Moisture wicking keeps you cool and dry
Taped neck and shoulders for durability; Tubular rib collar for better stretch and recovery
Feels soft to the touch; Tag free; Lays flat
5 pack = SM XL; 4 pack = 2X (Colors may vary)"

"""

stopWords = list(STOP_WORDS)

nlp = spacy.load('en_core_web_sm')

doc = nlp(text)

tokens =[token for token in doc]

wordFrequencies = {}

for word in tokens:
    wordLower = word.text.lower()
    if (wordLower not in stopWords) and (wordLower not in punctuation):
        if wordLower not in wordFrequencies.keys():
            wordFrequencies[wordLower] = 1
        else:
            wordFrequencies[wordLower] += 1

print(wordFrequencies)