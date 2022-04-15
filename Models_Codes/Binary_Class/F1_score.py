# Accuracy evaluation metrics using F1_score

# use formulae-> (2*p*r)/(p+r) , it is the harmonic mean.

from Precision import precesion
from Recall import recall

def f1_score_val(y_true,y_pred):
    p = precesion(y_true,y_pred)
    r = recall(y_true,y_pred)
    f1= (2*p*r)/(p+r)
    return f1


