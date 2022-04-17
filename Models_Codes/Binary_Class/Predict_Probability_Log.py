# Class Prediction Probabilty evaluation metric using log mean

# probability using predict_log_proba

'''
The predicted class log-probabilities of an input sample is computed as
the log of the mean predicted class probabilities of the trees in the
forest.
'''
from sklearn.ensemble import RandomForestClassifier

def predict_probability_log_class(test_X,self):
    pr = self.predict_log_proba(test_X)
    return pr