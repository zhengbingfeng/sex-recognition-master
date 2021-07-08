from sklearn.metrics import plot_confusion_matrix
from sklearn.metrics import classification_report
from sklearn.preprocessing import label_binarize
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
from itertools import cycle
import directory as dirt
from scipy import interp
import numpy as np
from sklearn import svm, datasets
from sklearn.model_selection import train_test_split
def plot_roc(X_train, X_test, y_train, y_test, classifier, method_name):
    
    class_names = ['male', 'female']
    y_train = label_binarize(y_train, classes=class_names)
    y_test = label_binarize(y_test, classes=class_names)
    X = np.concatenate([X_train, X_test])
    y = np.concatenate([y_train, y_test])
    n_classes = y.shape[1] 
    y_score = classifier.predict_proba(X_test)
    #y_score = classifier.fit(X_train, y_train).decision_function(X_test)
    print(y_score.shape)
    
    fpr = dict()  # 伪阳性率
    tpr = dict()  # 真阳性率
    roc_auc = dict()
    for i in range(n_classes):
        fpr[i], tpr[i], _ = roc_curve(y_test[:, i], y_score[:, i])
        roc_auc[i] = auc(fpr[i], tpr[i])
    plt.figure()
    lw = 2
    plt.plot(fpr[i], tpr[i], color='darkorange',
          lw=lw, label='ROC curve (area = %0.2f)' % roc_auc[i])
    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic to Binary Classification')
    plt.legend(loc="lower right")
    plt.savefig(dirt.Dirt.pic_path+method_name+'_roc.jpg')