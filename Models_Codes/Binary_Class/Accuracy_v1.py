# Accuracy evaluation metrics


def accuracy_ver1(y_true,y_pred):
    sum =0
    for i in range(0,len(y_true)):
        if y_true[i]==y_pred[i]:
            sum+=1
    return sum/len(y_true)