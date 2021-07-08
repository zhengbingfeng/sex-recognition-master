# 公用目录
class Dirt:
    # 生成中间文件的目录
    my_eigenface_path = 'data/my_eigenfaces/'
    # 原始二进制图片目录
    raw_data_path = 'data/raw_data/'
    # 二进制图片恢复成jpg格式后的存放目录
    restored_path = 'data/restored_data/'
    # 原始二进制训练、测试集及其对应标签目录
    raw_label_path = 'data/raw_label/'
    # 存放纯HOG特征预处理结果之后的文件目录
    my_hog_eigenface_path = my_eigenface_path + 'hog/'
    # 存放HOG+PCA后特征降维结果之后的文件目录
    my_hog_pca_eigenface_path = my_eigenface_path + 'hog_pca/'
    # 存放纯ResNet后特征预处理结果之后的文件目录
    my_resnet_eigenface_path = my_eigenface_path + 'resnet/'
    # 存放ResNet+KPCA后特征降维结果之后的文件目录
    my_resnet_kpca_eigenface_path = my_eigenface_path + 'resnet_kpca/'
    # 输出测试结果图片的文件目录
    pic_path = 'image/'


# 将全部图片整合，并读成矩阵形式进行存放
ri_path = Dirt.my_eigenface_path + 'readImage'
# 数据索引目录
index_path = Dirt.my_eigenface_path + 'index'
# 原始数据训练集标签文件路径
faceDR_path = Dirt.raw_label_path + 'faceDR'
# 原始数据测试集标签文件路径
faceDS_path = Dirt.raw_label_path + 'faceDS'
# 全部标签整合后的csv文件路径
faceD_csv_path = Dirt.my_eigenface_path + 'faceD.csv'


class HOGFile:
    # 存放纯HOG特征预处理结果之后的文件目录
    _path = Dirt.my_hog_eigenface_path
    # 经过纯HOG特征预处理后的训练集文件存放路径
    faceR_path = _path + 'faceR_hog'
    # 经过纯HOG特征预处理后的测试集文件存放路径
    faceS_path = _path + 'faceS_hog'
    # 经过纯HOG特征预处理后的训练集标签路径
    faceDR_path = _path + 'faceDR_hog.csv'
    # 经过纯HOG特征预处理后的测试集标签路径
    faceDS_path = _path + 'faceDS_hog.csv'


class HOG_PCAFile:
    # 存放HOG+PCA特征降维结果之后的文件目录
    _path = Dirt.my_hog_pca_eigenface_path
    # 经过HOG+PCA特征降维后的训练集文件存放路径
    faceR_path = _path + 'faceR_hog_pca'
    # 经过HOG+PCA特征降维后的测试集文件存放路径
    faceS_path = _path + 'faceS_hog_pca'
    # 经过HOG+PCA特征降维后的训练集标签路径
    faceDR_path = _path + 'faceDR_hog_pca.csv'
    # 经过HOG+PCA特征降维后的测试集标签路径
    faceDS_path = _path + 'faceDS_hog_pca.csv'


class ResnetFile:
    # 存放纯ResNet特征预处理结果之后的文件目录
    _path = Dirt.my_resnet_eigenface_path
    # 经过纯ResNet特征预处理后的训练集文件存放路径
    faceR_path = _path + 'faceR_resnet'
    # 经过纯ResNet特征预处理后的测试集文件存放路径
    faceS_path = _path + 'faceS_resnet'
    # 经过纯ResNet特征预处理后的训练集标签路径
    faceDR_path = _path + 'faceDR_resnet.csv'
    # 经过纯ResNet特征预处理后的测试集标签路径
    faceDS_path = _path + 'faceDS_resnet.csv'


class Resnet_KPCAFile:
    # 存放ResNet+KPCA特征预处理结果之后的文件目录
    _path = Dirt.my_resnet_kpca_eigenface_path
    # 经过ResNet+KPCA特征预处理后的训练集文件存放路径
    faceR_path = _path + 'faceR_resnet_kpca'
    # 经过ResNet+KPCA特征预处理后的测试集文件存放路径
    faceS_path = _path + 'faceS_resnet_kpca'
    # 经过ResNet+KPCA特征预处理后的训练集标签路径
    faceDR_path = _path + 'faceDR_resnet_kpca.csv'
    # 经过ResNet+KPCA特征预处理后的测试集标签路径
    faceDS_path = _path + 'faceDS_resnet_kpca.csv'