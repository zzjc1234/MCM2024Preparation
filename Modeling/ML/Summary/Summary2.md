# Summary2

Author: Zhaojiacheng Zhou

由于整理自matlab英语课程，如果发现中英文有出入，请以英语版本为准

---

## Menu

1. Introduction
2. Classification Learner App
3. k Nearest Neighbor Classification
4. Classification Trees
5. Naive Bayes Classification
6. Discriminant Analysis
7. Support Vector Machines
8. Multiclass Support Vector Machines
9. Neural Networks

---

### Introduction

- Typical machine learning workflow

![workflow](src/matlabMLflow.png)

---

### Classification Learner App

- Intro  
  “Classification Learner App”应用程序训练模型对数据进行分类。使用这个应用程序，可以使用各种分类器探索有监督的机器学习。

- 流程  
  1. 选择需要测试的模型or算法
  2. 用训练集训练模型
  3. 选择表现较好的几个算法
  4. 调整超参再次训练
  5. 分析原因

---

### k Nearest Neighbor Classification

- Intro  
  对新样本进行分类最直接的方法之一是找到与新样本相似的已知样本，并将新样本分配到同一类。这是k近邻分类的基本思想。  
  在使用这种方法时，我们不必对数据的底层分布做任何假设。
- 重要参数
  - NumNeighbors: Number of neighbors used for classification. (Default: 1)
  - Distance: Metric used for calculating distances between neighbors.
  - DistanceWeight: Weighting given to different neighbors.
  - Standardize: normalize the data

  The "cosine" distance metric works well for “wide” data (more predictors than observations) and data with many predictors.

---

### Classification Trees

- Intro

    机器学习中，决策树是一个预测模型；它代表的是对象属性与对象值之间的一种映射关系。树中每个节点表示某个对象，而每个分叉路径则代表的某个可能的属性值，而每个叶结点则对应从根节点到该叶节点所经历的路径所表示的对象的值。决策树仅有单一输出，若欲有复数输出，可以建立独立的决策树以处理不同输出。数据挖掘中决策树是一种经常要用到的技术，可以用于分析数据，同样也可以用来作预测。

- 重要步骤

  - 节点

    一个决策树包含三种类型的节点：
    1. 决策节点：通常用矩形框来表示
    2. 机会节点：通常用圆圈来表示
    3. 终结点：通常用三角形来表示

  - 剪枝

    剪枝是决策树停止分支的方法之一，剪枝有分预先剪枝和后剪枝两种。

    - 预先剪枝

        预先剪枝是在树的生长过程中设定一个指标，当达到该指标时就停止生长，这样做容易产生“视界局限”，就是一旦停止分支，使得节点N成为叶节点，就断绝了其后继节点进行“好”的分支操作的任何可能性。不严格的说这些已停止的分支会误导学习算法，导致产生的树不纯度降差最大的地方过分靠近根节点。

    - 后剪枝

        后剪枝中树首先要充分生长，直到叶节点都有最小的不纯度值为止，因而可以克服“视界局限”。然后对所有相邻的成对叶节点考虑是否消去它们，如果消去能引起令人满意的不纯度增长，那么执行消去，并令它们的公共父节点成为新的叶节点。这种“合并”叶节点的做法和节点分支的过程恰好相反，经过剪枝后叶节点常常会分布在很宽的层次上，树也变得非平衡。后剪枝技术的优点是克服了“视界局限”效应，而且无需保留部分样本用于交叉验证，所以可以充分利用全部训练集的信息。但后剪枝的计算量代价比预剪枝方法大得多，特别是在大样本集中，不过对于小样本的情况，后剪枝方法还是优于预剪枝方法的。

  - 优点

    决策树易于理解和实现

    数据准备简单，构建快速

    易于通过静态测试来对模型进行评测，可以测定模型可信度（如果给定一个观察的模型，那么根据所产生的决策树很容易推出相应的逻辑表达式）

  - 缺点

    1. 对连续性的字段比较难预测。
    2. 对有时间顺序的数据，需要很多预处理的工作。
    3. 当类别太多时，错误可能就会增加的比较快。
    4. 一般的算法分类的时候，只是根据一个字段来分类。

- 重要参数
  - SplitCriterion（分割准则）：用于确定每个级别的最佳分割的公式
  - MinLeafSize：每个叶节点的最小观测数
  - maxnumsplitting：决策树中允许的最大拆分数

- Tips

    当有大量数据丢失时，树是一个很好的选择

---

### Naive Bayes Classification

- Intro

  kNN模型和决策树对底层数据的分布不做任何假设。

  如果我们假设数据集来自底层分布，我们可以将数据视为统计样本。这可以减少异常值对模型的影响。

  朴素贝叶斯分类器假设每个类中的predictor是独立的。对于相对简单的问题，这个分类器是一个很好的选择。

- 重点
  - 用数据集生成先验概率，再计算后验概率。通过后验概率确定数据属于哪个聚类

- 优点

    根据模型的分布会计算出一个准确的概率而不是如knn决策树等算法一般做近似处理，多余噪声等因素抗干扰性强

- 局限

    要求变量独立，如果变量有相互关联则可信度以及效果可能不理想。

---

### Discriminant Analysis

- Intro

  与朴素贝叶斯相似，判别分析的工作原理是假设每个预测类别中的观测值可以用正态概率分布建模。然而，每个预测器都不存在独立假设。因此，每个类都拟合了多元正态分布。

- 算法思想

  - 判别分析使用训练集决定preditor之间的边界的位置。

  - 判别分析将训练集中的观测值视为多维正态分布中的样本。

  - 用n维正态分布拟合一个类中的观测值。这涉及到为每个类计算均值向量和协方差矩阵。这决定了分布的中心和形状。
  - 拟合分布后，可以根据概率相同的点画出类别之间的边界

- 重要参数
  - 判别类型：线性or二元
  - 在线性边界中包含预测因子的系数阈值
  - 用于估计线性DA的协方差矩阵的正则化
  
- Tips：  
  线性判别分析适用于“广泛”数据(预测因子多于观测值)

- 优势

  抗噪声能力强

---

### Support Vector Machines

- Intro

  支持向量机是一种二元分类的算法，通过寻找分离所有数据点的“最佳”超平面来对数据进行分类

- 算法思想

  对每一种可能的超平面，我们将它进行平移，直到它与空间中的样本向量相交。我们称这两个向量为支持向量，之后我们计算支持向量到该超平面的距离d，分类效果最好的超平面应该使d最大。

- 分类
  - 线性可分
    - 寻找最优分类超平面，即离两类所有的观察值距离最远的线
  - 线性不可分
    - 软间隔
      - 设置容错率
    - 硬间隔
      - 寻找合适的核函数

- 重要参量
  - 数据集
  - 间隔类型
  - 容错率
  - 核函数
  - 核函数应用前的放缩
  - 归一化方式

---

### Multiclass Support Vector Machines

- Intro

  支持向量机是针对二元分类的算法，multiclass支持向量机在支持向量机的基础上创建error-correcting output codes (ECOC)分类器从而达到处理多个分类

- 创建步骤

  1. 创建二元分类模版
  2. 创建MSVM model

- 重要参数

  与SVM相同

---

### Neural Networks

- Intro

  神经网络通过一组连接的神经元模拟人脑的行为。这些网络通过反复试验来调整神经元之间的连接，从而学会识别模式。

  这种方法不对数据做任何假设。但是它要求数据是规范化的。

- 算法

  - 分层
    - Input Layer(输入层): One for each predictor variable
    - Hidden Layer(处理层)
    - Output Layer(输出层) : One for each reponse class

  - 流程
    1. 输入
    2. 输入层中每一个节点将信息传递给每一个处理层节点
    3. 根据数据的权重（神经元连接强度？）计算加权平均，并作为节点方程的输入
    4. 处理层中每一个节点将信息传递给每一个输出层节点
    5. 计算加权平均并带入方程
    6. 输出结果（一般[0,1]区间）

  - 训练正反馈神经网络
    - 分割数据集

      通过将数据集分割为训练集和验证集来防止神经网络过拟合，最后通过测试集合来评估模型

  - 重要参数
    - Layer Size：层节点个数
    - Activation：每个充分连接的层的activation function
    - Validation Data：验证集
    - Validation Patience: 遭遇连续无法提升模型质量，停止迭代的次数

  - Tips

    Neural networks work well for "tall" data (more observations than predictors).
