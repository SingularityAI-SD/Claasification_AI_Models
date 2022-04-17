# Accuracy evaluation metrics using Log_Loss

# use formulae-> -1.0*(target*log(prediction) +(1-target)*log(1-prediction))

# target is 0 or 1, prediction is probability of sample belonging to 1

import numpy as np

loss=[]
def log_loss(y_true,y_prob):
    epsilon = 1e-15 #-> 1 x 10^-15
    for i,j in zip(y_true,y_prob):
        j = np.clip(j,epsilon,1-epsilon)
        temp_loss = -1.0*(i*np.log(j) +(1-i)*np.log(1-j))
        loss.append(temp_loss)
    return np.mean(loss)