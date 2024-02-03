# Collection

Description: Plan for model collection.

---

## Biology

- Shannon-Wiener Index
- ICV
- Lotka-Volterra model
- logistic sigmoid
- Simpson Index

## Correlation

- Spearman

  We can use `spearman` to calculate the correlation of variables.

We can also use another method included in the `pandas.correlation`

## ODE

<!-- INFO: for ODE problem, we can simply use scipy to solve equation. However, The method is still meaningful in intelpreting our model -->

- Euler method
- Runge-Kutta method

## Merge

- AHP
  - Intro

    AHP is short for Analytic hierarchy process. Personally, I think this method is quite subjective.

  - Workflow
    - Model the problem as a hierarchy

      Usually, we model the problem into a hierarchy with following three levels:

      - Goal: The problem we want to solve
      - Criteria: Factor which matters in the decision
      - Alternative: The alternative to reach the goal

    - Evaluate the hierarchy (Create a judge matrix)

      In this part, we need to construct a judge matrix subjectively. For each entry in the matrix eg. a_{ij}, it represents the priority between two criteria. The matrix can be not consistent.

    - Evaluate the matrix

      We use the formula to evaluate the consistency of the alternative.

      $$CI=\frac{\lambda_{max}-n}{n-1}$$

      where, $\lambda$ is the largest eigenvalue of the matrix, n is the dimension of the matrix.

      RI can be found by checking the table.

      To evaluate the final result, we need to evaluate each judge matrix and overall consistency with formula

      $$CR=\frac{\sum^{m}_{j=1}W_{j} CI_{j}}{W_{j}RI_{j}}$$

## Classification

### Supervised

- svm
- sgd
- knn
- naivebyes
- discriminant analysis
- tree

### Unsupervised

- kmeans
- linkage
- gmm
- manifold

## Regression

- liner
- logistic
- tree
- svm
- gaussian process regression

## Misc

- PIE
- WPZ HSZ LGZ
