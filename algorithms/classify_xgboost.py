from xgboost.sklearn import XGBClassifier
from fileio import readFaceRS
import algorithms.plot as plot


def predict(X_train, X_test, y_train, y_test, method_name):
    print('Start XGBoost predicting...')


    xgb =XGBClassifier()
    xgb.fit(X_train, y_train.values.ravel())

    print('Accuracy score of xgb: ' + '%.3f' %
          xgb.score(X_test, y_test))

    plot.plot_roc(X_train, X_test, y_train, y_test,
                  xgb, method_name)


def run(method_readFaceRS='resnet'):
    # 读取经过上一步特征处理处理的四个输出(ResNet/ResNet_kpca)
    X_train, X_test, y_train, y_test = readFaceRS(method_readFaceRS)

    # 取age
    y_train_sex = y_train[['sex']]
    y_test_sex = y_test[['sex']]

    method_name = method_readFaceRS + '_xgb'
    predict(X_train, X_test, y_train_sex, y_test_sex, method_name)
