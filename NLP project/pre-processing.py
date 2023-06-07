##################################### Importing libraries #####################################

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

##################################### Operation Functions #####################################

def remove_punct(text):
    text = "".join([char for char in text if char not in string.punctuation])
    return text

# Remove Alpha Numeric
def remove_alphanumeric(text):
    text = ''.join([i for i in text if not i.isdigit()])
    return text

stop = stopwords.words('english')

def remove_stopwords(text):
    text = [word for word in text.split() if word.lower() not in (stop)]
    return " ".join(text)