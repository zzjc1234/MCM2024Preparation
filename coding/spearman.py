#!/usr/local/anaconda3/bin/python

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def spearman(frame, features):
    """
    spearman released by zzjc
    """
    spr = pd.DataFrame()
    spr["feature"] = features
    spr["spearman"] = [frame[f].corr(frame["SalePrice"], "spearman") for f in features]
    spr = spr.sort_values("spearman")
    plt.figure(figsize=(6, 0.25 * len(features)))
    sns.barplot(data=spr, y="feature", x="spearman", orient="h")


import scipy.stats as stats

data = {"A": [1, 2, 3, 4, 5], "B": [5, 4, 3, 2, 1], "C": [1, 2, 1, 2, 1]}
df = pd.DataFrame(data)

# 使用spearmanr计算整个数据框的Spearman相关系数矩阵
correlation_matrix, p_value_matrix = stats.spearmanr(df)
