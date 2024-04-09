#!c:/users/heispv/miniconda3/lib/site-packages python3
import sys
import numpy as np

def get_data(predfile):
    preds = []
    f = open(predfile)
    for line in f:
        v = line.rstrip().split()
        v[1] = float(v[1])
        v[2] = int(v[2])
        preds.append(v)
    return preds

def get_cm(preds, th):
    cm = np.zeros((2, 2))
    for pred in preds:
        p = 0
        r = pred[2]
        if pred[1] <= th:
            p = 1
        cm[p][r] += 1
    return cm

def get_mcc(cm):
    tp = cm[1][1]
    tn = cm[0][0]
    fp = cm[0][1]
    fn = cm[1][0]
    mcc = (tn * tp) + (fn * fp)
    d = np.sqrt((tp+fn)*(tp+fp)*(fp+tn)*(fn+tn))
    return mcc / d


if __name__ == '__main__':
    predfile = sys.argv[1]
    th = 0.5
    if len(sys.argv) > 2:
        th = float(sys.argv[2])
    preds = get_data(predfile)
    print(preds)
    cm = get_cm(preds, th)
    print(cm)
    mcc = get_mcc(cm)
    print(mcc)
