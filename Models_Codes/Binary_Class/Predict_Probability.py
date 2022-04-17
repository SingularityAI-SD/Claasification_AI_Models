# Class Prediction Probabilty evaluation metric

# probability using predict_log_proba

'''
It is the mean predicted class probabilities of the trees in the forest.
The class probability of a single tree is the fraction of samples of the same class in a leaf.
'''
from sklearn.ensemble import RandomForestClassifier

def predict_probability_class(test_X,self):
    pr = self.predict_proba(test_X)
    return pr
