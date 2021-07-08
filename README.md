# sex-recognition-master
基于人脸图像利用SVM和XGBoost进行性别分类
## 数据集来源

数据集地址：[Face-Recognition-Project](https://courses.media.mit.edu/2004fall/mas622j/04.projects/faces/)

1. 下载官网上的rawdata.zip和faces.zip并解压；
2. 在项目根目录下创建data父目录，以及data/raw_data和data/raw_label两个子目录；
3. 将rawdata.zip解压后的文件夹中的图片二进制文件拷贝到data/raw_data中，
   并将faces.zip解压后的faceDR、faceDS标签文件拷贝到data/raw_label中；
4. 利用程序pretreatment.ipynb将上述标签文件全部整合，重新按照7：3的比例划分训练集与测试集；

## 运行环境

- 操作系统：Windows 10；
- 集成开发环境：Jupyter Notebook
- 必要的工具：见 配置要求.txt

## 运行说明
1.先运行pretreatment.ipynb对原始数据进行处理；
2.运行hog_svm.ipynb：对数据集进行HOG特征提取再用SVM进行分类；
  运行hog_pca_svm.ipynb：对数据集进行HOG特征提取，再进行特征降维，最后用SVM进行分类；
  运行resnet_xgboost.ipynb：对数据集进行ResNet50特征提取再用XGBoost进行分类；
  运行resnet_kpca_xgboost.ipynb：对数据集进行ResNet50特征提取，再进行特征降维，最后用XGBoost进行分类；
  
