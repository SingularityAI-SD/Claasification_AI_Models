# Accuracy evaluation metrics
# TP,TN,FP,FN


def true_positive(y_true,y_pred):
    tp =0
    for i in range(0,len(y_true)):
        if y_true[i]==1 and y_pred[i]==1:
            tp+=1
    return tp

def true_negative(y_true,y_pred):
    tn =0
    for i in range(0,len(y_true)):
        if y_true[i]==0 and y_pred[i]==0:
            tn+=1
    return tn

def false_positive(y_true,y_pred):
    fp =0
    for i in range(0,len(y_true)):
        if y_true[i]==0 and y_pred[i]==1:
            fp+=1
    return fp

def false_negative(y_true,y_pred):
    fn =0
    for i in range(0,len(y_true)):
        if y_true[i]==1 and y_pred[i]==0:
            fn+=1
    return fn



# use formulae-> acc_score = tp+tn/(tp+tn+fp+fn)

# works only for binary classification

def accuracy_ver2(y_true,y_pred):
    tp = true_positive(y_true,y_pred)
    tn = true_negative(y_true,y_pred)
    fp = false_positive(y_true,y_pred)
    fn = false_negative(y_true,y_pred)
    return ((tp+tn)/(tp+tn+fp+fn))