# Accuracy evaluation metrics using Macro_Average_Precision

import numpy as np
from Accuracy_v2 import true_positive,false_positive

def macro_avg_pr(y_true,y_pred):
    num_class= len(np.unique(y_true))
    pr =0 # precesion=0
    for i in range(num_class):
        true = [1.0 if j==i else 0.0 for p in y_true for j in p]
        pred = [1.0 if j==i else 0.0 for p in y_pred for j in p]

        # true positive and false positive for the current class
        tp = true_positive(true,pred)
        fp = false_positive(true,pred)

        # precision for current class
        precision = tp/(tp+fp)

        # add the precision for all the class
        pr+=precision

    # return avg precision
    precision/= num_class
    return precision
