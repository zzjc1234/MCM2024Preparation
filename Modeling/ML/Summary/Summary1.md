# Summary1

Author: Zhaojiacheng Zhou

由于整理自matlab英语课程，如果发现中英文有出入，请以英语版本为准

---

## Menu

1. Low Dimensional Visualization
2. k-Means Clustering
3. Gaussian Mixture Models
4. k-means VS GMM
5. Interpreting the Clusters
6. Hierarchical Clustering

---

### Low Dimensional Visualization

- PCA and CMD
  - Introduction

    PCA(Principle Component Analysis)和CMD(Classical Mutidimensional Scaling)是常用的多变量分析方法

  - 应用场景

    PCA和CMD可以在保证不失去大量信息的情况下对多变量数据or矩阵进行降维处理

  - 详细说明
    - CMD  
      CMD通常需要先计算观察值（observations）的成对距离（pairwise distance）从而生成相异度向量（dissimilarity vector)再计算重构后的矩阵（记重构后的矩阵为x）以及x*x'的本征值e。可以使用本征值e来确定对x中的点的低维近似是否提供了数据的合理表示。如果帕累托图中显示前p个特征值显著大于其余的特征值，则这些点被前p维(即x的前p列)很好地近似
    - PCA  
      PCA主成分分析的机理主要是是将原来很多具有相关性的一系列指标(p个指标)重新组合成一组较少个数的互不相关的综合指标来代替原来的指标。利用挑选的一组合适的权重来得到一个原随机变量的主成分[[link](https://anl.sjtu.edu.cn/mcm/docs/name/主成分分析PCA)]

      - 重要参数：  
        1. 原始数据：m行（观察值）n列（变量）
        2. Principal component coefficients(主成分系数）：p*p矩阵，每一列包含一个主成分相关系数。
        3. Principal component scores（主成分得分）：
        4. Principal component variances（主成分方差）：
        5. Hotelling’s T-Squared Statistic（霍特林T$^2$统计量）: A statistical measure of the multivariate distance of each observation from the center of the data set.
        [[link1](https://online.stat.psu.edu/stat505/lesson/7/7.1/7.1.15)]
        [[link2](src/T-squared-Test.pdf)]
        6. explained（解释方差占总方差的百分比）:Percentage of the total variance explained by each principal component
        7. mu(估计的均值):Estimated means of the variables in input data
      - 应用：  
        1. 使用explained（解释方差占总方差的百分比）绘制 Pareto chart（帕累托图）以判断哪几个principle component的contribution比较大，确定后续研究对象
        2. 确定研究的principle component之后绘制散点图或者运用聚类进行分类

---

### k-Means Clustering

- Intro
  >>k-means聚类是一种基于划分的动态聚类算法，同时也是一种具有较大影响力的无监督学习算法。该算法的优点是思想简单易行，时间复杂性接近线性，对大规模数据的挖掘具有高效性和可伸缩性，在工况分类等领域中有着广泛的应用。

- 重要参数
  - data matrix
  - 聚类数量
  - 簇中心的初始值
  - 测度（metirc）
  - 输出：聚类索引 ( eg.observation（1，1）属于1号聚类，则索引为1 ）

- 优化策略
  - 选择合适的测度(option: `"Distance"`)
  - 初始化簇中心时，选择合适的值(option: `"Start"`)
  - 以不同的簇中心，多次计算(option:`"Replicate"`)

---

### Gaussian Mixture Models

- Intro  
  Gaussian Mixture Models （高斯混合模型）是另一类聚类算法。GMM聚类包括拟合多个n维正态分布到数据，并使用这些分布将每个观测值分配到一个聚类中。

- 重要参数
  - 建立模型的数据集
  - 拟合高斯混合模型时使用的分量数(正整数)。eg，如果指定k = 3，则该软件拟合一个具有三个不同均值、协方差矩阵和数据(X)分量比例的高斯混合模型。
  - 输出：一个高斯混合分布模型

- 生成聚类步骤
  1. 选择合适的参数建立模型
  2. 选择合适的参数，通过计算每个观测到的每个成分的后验概率进行概率聚类,得到聚类和模型中每个高斯混合分量的后验概率

- 优化策略
  - 增加迭代次数
  - 选择合适的方差
  - 选取合适的 Regularization Value
  - ...

---

### k-means VS GMM

- Kmeans的缺点

>>2维k-means模型的本质是，它以每个簇的中心为圆心，簇中点到簇中心点的欧氏距离最大值为半径画一个圆。这个圆硬性的将训练集进行截断。而且，k-means要求这些簇的形状必须是圆形的。因此，k-means模型拟合出来的簇（圆形）与实际数据分布（可能是椭圆）差别很大，经常出现多个圆形的簇混在一起，相互重叠。总的来说，k-means存在两个缺点，使得它对许多数据集（特别是低维数据集）的拟合效果不尽如人意：
>>
>>1. 类的形状不够灵活，拟合结果与实际相差较大，精度有限。
>>2. 样本属于每一个簇的概率是定性的，只有是与否，不能输出概率值。应用中缺少鲁棒性

其中第一点可以通过选择合适的metric解决

- GMM

>>高斯混合模型试图找到多维高斯模型概率分布的混合表示，从而拟合出任意形状的数据分布。因为GMM模型并不是通过硬截断进行分割类别，而是通过高斯平滑模型进行估计的。所以将每个点的概率进行可视化时，散点图并不是严格成椭圆形状的如果允许使用全部的协方差类型，则可以拟合任意形状的分布。
>>
>>GMM模型的本质并不是聚类，而是得到一个，能够生成当前样本形式的分布

[[ref link](https://zhuanlan.zhihu.com/p/81255623)]

---

### Interpreting the Clusters

- Parallel Coordinates(平行坐标图)  
    显示不同聚类在各个变量下的观测值

- Cross-Tabulation(交叉表)
  - Intro  
    在一些数据集中，观测值已经有了与之相关的类别。可以使用Cross-Tabulation(交叉表)来研究原始类别之间的集群分布
- Heatmap（热力图）
  - 可视化数据（eg.可视化cross table中的数据）

- Silhouette Plots(轮廓图)
  - Intro  
    在使用聚类技术(如k-means和高斯混合模型)时，必须指定聚类的数量。然而，对于高维数据，很难确定最佳簇数。  
    可以使用轮廓值来判断集群的质量。一个观测值的轮廓值是一个标准化的度量(介于-1和+1之间)，用于与不同聚类中的观测值相比，该观测值与同一聚类中的其他观测值的接近程度

    轮廓图显示每个观测的轮廓值，按聚类分组。大多数观测值具有高廓形值的聚类方案是可取的，即正值面积越大越合理
  - `evalclusters` function  
    - Example：

    ```matlab
    %try the k value from 2 to 5, evaluate with sihouette plot
    clustev = evalclusters(X,"kmeans","silhouette","KList",2:5)
    ```

---

### Hierarchical Clustering

- Function `linkage`  
  使用Function `linkage`创建层次树。  
  可选的第二个和第三个输入指定了计算集群之间距离(默认为“single”)和计算点之间距离(默认为“euclidean”)的方法。

- Function `dendrogram`  
  可以使用树状图函数来可视化层次结构。

- 应用
  可以根据链接距离Z使用聚类函数将观测值分配到组中
