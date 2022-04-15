# Accuracy evaluation metrics using Precesion

from Accuracy_v2 import true_positive,false_positive

# use formulae-> tp/(tp+fp)
def precesion(y_true,y_pred):
    tp = true_positive(y_true,y_pred)
    fp = false_positive(y_true,y_pred)
    return (tp/(tp+fp))