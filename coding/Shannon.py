#!/usr/local/anaconda3/bin/python

import numpy as np

def shannon_wiener_index(relative_abundances):
    """
    计算Shannon-Wiener Index

    Parameters:
    relative_abundances (array-like): 物种的相对丰度列表或数组

    Returns:
    float: Shannon-Wiener Index
    """
    p_values = np.array(relative_abundances)
    p_values_normalized = p_values / p_values.sum()  # 将相对丰度归一化
    shannon_index = -np.sum(p_values_normalized * np.log2(p_values_normalized))
    return shannon_index

# 示例数据
relative_abundances = [0.2, 0.3, 0.1, 0.4]

# 计算Shannon-Wiener Index
shannon_index = shannon_wiener_index(relative_abundances)

print("Shannon-Wiener Index:", shannon_index)
