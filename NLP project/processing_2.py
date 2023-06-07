import re #regular expression
import spacy
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer
import string
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
nlp = spacy.load('en_core_web_sm')


# find the number of unique words in each question
def unique_words(text):
    doc = nlp(text)
    unique_words = set([token.text for token in doc if token.is_stop != True and token.is_punct != True])
    return len(unique_words)

# find common words in each question
def common_words(text):
    doc = nlp(text)
    common_words = set([token.text for token in doc if token.is_stop == True and token.is_punct == True])
    return len(common_words)