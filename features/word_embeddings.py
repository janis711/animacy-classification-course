# Imports 
from sklearn.base import BaseEstimator
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Class WordEmbeddings
# Code snippet sourced from: Karsdorp et al. (2015)  “Animacy Detection in Stories”
# Source: https://github.com/fbkarsdorp/animacy-detection/blob/master/experiment.py

class WordEmbeddings(BaseEstimator):
    def __init__(self, model, scale=False):
        self.model = model
        self.scale = scale

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # x is a document, word[0] is the word token
        transformed_X = np.vstack([self.model[word[0].lower()] if word[0].lower() in self.model else
                          np.zeros(300) for x in X for word in x]) # Here we changed 'np.zeros(self.mode.layer1_size)' to 'np.zeros(300)' 
        # print(f'Shape of Word Embedding Features: {transformed_X.shape}')
        return transformed_X

    def fit_transform(self, X, y=None):
        self.fit(X, y)
        if self.scale:
            return MinMaxScaler().fit_transform(self.transform(X))
        return self.transform(X)