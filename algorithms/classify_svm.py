from fileio import readFaceRS
from sklearn.svm import SVC
import algorithms.plot as plot


def predict(X_train, X_test, y_train, y_test, method_name):
    print('Start SVM predicting...')

    svm = SVC(kernel='rbf', probability=True)
    svm.fit(X_train, y_train.values.ravel())

    print('Accuracy score of svm: ' + '%.3f' %
          svm.score(X_test, y_test))

    plot.plot_roc(X_train, X_test, y_train, y_test,
                  svm, method_name)


def run(method_readFaceRS='hog'):
    # 读取经过上一步特征处理处理的四个输出(hog/hog_pca)
    X_train, X_test, y_train, y_test = readFaceRS(method_readFaceRS)

    # 取age
    y_train_sex = y_train[['sex']]
    y_test_sex = y_test[['sex']]

    method_name = method_readFaceRS + '_svm'
    predict(X_train, X_test, y_train_sex, y_test_sex, method_name)
