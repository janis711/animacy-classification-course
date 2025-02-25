# Imports
from sklearn.base import BaseEstimator
import numpy as np
import scipy.sparse as sp

# Class FeatureStacker
# Code snippet sourced from: Karsdorp et al. (2015)  “Animacy Detection in Stories”
# Source: https://github.com/fbkarsdorp/animacy-detection/blob/master/experiment.py

class FeatureStacker(BaseEstimator):
    """Stacks several transformer objects to yield concatenated features.
    Similar to pipeline, a list of tuples ``(name, estimator)`` is passed
    to the constructor.
    """
    def __init__(self, *transformer_list):
        self.transformer_list = transformer_list

    def get_feature_names(self):
        pass

    def fit(self, X, y=None):
        for name, trans in self.transformer_list:
            trans.fit(X, y)
        return self

    def transform(self, X):
        features = []
        for name, trans in self.transformer_list:
            feature_matrix = trans.transform(X)
            # print(f"Feature matrix shape for {name}: {feature_matrix.shape}")  
            features.append(feature_matrix)
        issparse = [sp.issparse(f) for f in features]
        if np.any(issparse):
            features = sp.hstack(features).tocsr()
        else:
            features = np.hstack(features)
        # print(f'Shape of All Features: {features.shape}')
        return features

    def fit_transform(self, X, y=None):
        self.fit(X, y)
        return self.transform(X)

    def get_params(self, deep=True):
        if not deep:
            return super(FeatureStacker, self).get_params(deep=False)
        else:
            out = dict(self.transformer_list)
            for name, trans in self.transformer_list:
                for key, value in trans.get_params(deep=True).iteritems():
                    out['%s__%s' % (name, key)] = value
            return out