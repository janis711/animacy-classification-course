# Imports
from sklearn.feature_extraction import DictVectorizer
from sklearn.base import BaseEstimator

# Class to extract windowed features from documents/ texts
# Code snippet sourced from: Karsdorp et al. (2015)  “Animacy Detection in Stories”
# Source: https://github.com/fbkarsdorp/animacy-detection/blob/master/experiment.py

class Windower(BaseEstimator):

    def __init__(self, window_size=3):
        self.window_size = window_size
        self.fitted = False
        self.vectorizer = DictVectorizer(sparse=True)

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X_ = []
        n_fields = len(X[0][0])
        for d, doc in enumerate(X):
            for i, word in enumerate(doc):
                features = []
                for j in range(i + 1 - self.window_size, i): # original for j in range(i - self.window_size, i):
                    features.extend([None] * n_fields if j < 0 else doc[j])
                features.extend(word)
                for j in range(i + 1, i + self.window_size):
                    features.extend([None] * n_fields if j >= len(doc) else doc[j])
                
                X_.append({str(k): f for k, f in enumerate(features) if f != None})
        transform = (self.vectorizer.fit_transform if not self.fitted else
                     self.vectorizer.transform)
        self.fitted = True
        transformed_X = transform(X_)
        # print(f'Shape of Windower Features: {transformed_X.shape}')
        return transformed_X

    def fit_transform(self, X, y=None):
        self.fit(X, y)
        return self.transform(X)