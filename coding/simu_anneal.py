#!/usr/local/anaconda3/bin/python

import numpy as np


def simulated_annealing(
    problem, initial_solution, initial_temperature, cooling_rate, max_iterations
):
    current_solution = initial_solution
    current_energy = problem.evaluate(current_solution)

    for iteration in range(max_iterations):
        temperature = initial_temperature / (1 + cooling_rate * iteration)

        new_solution = problem.get_neighbor(current_solution)
        new_energy = problem.evaluate(new_solution)

        if new_energy < current_energy or np.random.rand() < np.exp(
            (current_energy - new_energy) / temperature
        ):
            current_solution = new_solution
            current_energy = new_energy

    return current_solution, current_energy


# 示例：旅行商问题
class TSPProblem:
    def __init__(self, cities):
        self.cities = cities

    def evaluate(self, solution):
        total_distance = 0
        for i in range(len(solution) - 1):
            total_distance += np.linalg.norm(
                self.cities[solution[i]] - self.cities[solution[i + 1]]
            )
        total_distance += np.linalg.norm(
            self.cities[solution[-1]] - self.cities[solution[0]]
        )
        return total_distance

    def get_neighbor(self, solution):
        # 生成新解的方式，这里采用随机交换两个城市的位置
        neighbor = solution.copy()
        idx1, idx2 = np.random.choice(len(neighbor), size=2, replace=False)
        neighbor[idx1], neighbor[idx2] = neighbor[idx2], neighbor[idx1]
        return neighbor


# 示例数据
cities = np.array([[0, 0], [1, 2], [2, 4], [3, 1], [4, 3]])

# 初始解、温度、退火率、最大迭代次数
initial_solution = np.arange(len(cities))
initial_temperature = 100.0
cooling_rate = 0.01
max_iterations = 1000

# 创建问题实例
tsp_problem = TSPProblem(cities)

# 运行模拟退火算法
final_solution, final_energy = simulated_annealing(
    tsp_problem, initial_solution, initial_temperature, cooling_rate, max_iterations
)

print("最终解:", final_solution)
print("最终能量 (总距离):", final_energy)

# INFO: Or we can simply use the function provided by scipy

from scipy.optimize import minimize
import numpy as np


# 示例：最小化一个简单的目标函数
def objective_function(x):
    return x[0] ** 2 + x[1] ** 2


# 初始解
initial_solution = np.array([1.0, 2.0])

# 调用scipy中的simulated_annealing函数
result = minimize(
    objective_function, initial_solution, method="anneal", options={"maxiter": 1000}
)

# 输出结果
print("最终解:", result.x)
print("最终目标函数值:", result.fun)
