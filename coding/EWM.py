#!/usr/local/anaconda3/bin/python

import numpy as np


def entropy_weight(matrix):
    """
    计算熵权法的权重

    Parameters:
    matrix (numpy.ndarray): 决策矩阵，每行代表一个样本，每列代表一个指标

    Returns:
    numpy.ndarray: 每个指标的权重
    """
    # 数据标准化
    normalized_matrix = matrix / matrix.sum(axis=0)

    # 计算信息熵
    entropy = -np.sum(normalized_matrix * np.log2(normalized_matrix), axis=0)

    # 计算权重
    weights = (1 - entropy) / np.sum(1 - entropy)

    # 归一化权重
    normalized_weights = weights / np.sum(weights)

    return normalized_weights


# 示例数据
decision_matrix = np.array([[3, 4, 2], [5, 2, 1], [1, 6, 4], [2, 5, 3]])

# 计算权重
weights = entropy_weight(decision_matrix)

print("熵权法计算的权重:", weights)
