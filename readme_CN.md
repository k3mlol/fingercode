## 基本信息
基于Gbaor滤波得指纹识别。看的[论文](https://www.researchgate.net/publication/261265221_FingerCode_A_filterbank_for_fingerprint_representation_and_matching)
FingerCode： A Filterbank for Fingerprint Representation and Matching
但是识别率低，因为计算参考点的方法很不好。

## 安装环境
需要opencv，这个[链接](http://www.jianshu.com/p/67293b547261) 我相信已经很好。
我用的是Python2.7

## 处理步骤

1. 识别参考点
2. 划分扇区
3. 归一化处理
4. 计算特征值
5. 存储特征值
6. 特征值比较，显示相似指纹


## 项目文件介绍
1. fingercode.py 是计算特征值
2. 1 and 2 folder 指纹图像使用FVC的数据库，里面包含指纹图像
3. DB.py 保存特征向量的数据库，使用sqlite3
4. Sector.py 划分扇区
5. Gabor.py Gabor滤波处理指纹图像
6. run.py 计算数据库里面的指纹特征值，然后显示相似得指纹图像
7. final.db 已经计算好得指纹fingercode
8. unused 没有的，学习使用
