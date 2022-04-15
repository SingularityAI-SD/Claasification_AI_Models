# Accuracy evaluation metrics using Recall

from Accuracy_v2 import true_positive,false_negative

# use formulae-> tp/(tp+fn)
def recall(y_true,y_pred):
    tp = true_positive(y_true,y_pred)
    fn = false_negative(y_true,y_pred)
    return (tp/(tp+fn))