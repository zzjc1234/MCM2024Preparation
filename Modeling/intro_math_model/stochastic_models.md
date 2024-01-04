# Stochastic Models

## Overview
- Stochastic Models
  - Definition: **Predictive** models for **random** phenomena
  - Characteristics
    - Detached from specific applications
    - Axiomatic structure within mathematics
    - Capture relevant aspects of phenomena
    - Enable deduction of predictions
  - Stochastic Processes
    - Definition: Collection of **random variables** indexed over a set
    - Characteristics
      - **State space**: Range of possible values
      - **Index set**: Parameter defining the variables
      - **Dependencies**: Relations among variables
  - Analysis Techniques
    - Mathematical methods for process analysis
    - Predictive capabilities for real-world phenomena

## Probability Distributions

### Variables and Densities
- **Random Variables**
  - Definition: Numerical representation of outcomes from random events
  - Types
    - **Discrete**: Finite or countable range (e.g., coin flip outcomes)
    - **Continuous**: Uncountably infinite range (e.g., temperature measurements)
- **Probability Distributions**
  - For Continuous Variables: Collection of probabilities for intervals on the real line
  - Role: Describe the likelihood of different outcomes
- **Probability Density Functions** (PDFs)
  - Purpose: Specify probability distributions for continuous variables
  - Characteristic: Area under the curve represents probability for an interval
- **Mean and Variance** (for continuous distribution)
  - mean
    - $\mu = \int_{-\infty}^{\infty} x f_X(x) \, dx$
  - variance
    - $\sigma^2 = \int_{-\infty}^{\infty} (x - \mu)^2 f_X(x) \, dx$
- **Parameter Estimation** (for an observed sample of $N$ values of $X$)
  - sample mean
    - $\hat{\mu} = \frac{1}{N} \sum_{i=1}^N x_i$
  - sample variance
    - _biased_
      - $\hat{\sigma}^2 = \frac{1}{N} \sum_{i=1}^N (x_i - \hat{\mu})^2$
    - **unbiased** (better, especially for small samples [why](https://math.stackexchange.com/questions/496627/the-difference-between-unbiased-biased-estimator-variance)) 
      - $\hat{\sigma}^2 = \frac{1}{N - 1} \sum_{i=1}^N (x_i - \hat{\mu})^2$

### Common Distributions

#### Discrete Distributions [see more](https://appliedmath.arizona.edu/sites/default/files/0f04d86a836182cbf608dfc86c7a70f5e5f6_0.pdf#%5B%7B%22num%22%3A143%2C%22gen%22%3A0%7D%2C%7B%22name%22%3A%22Fit%22%7D%5D)
TODO:
- **Bernoulli Distribution**
- **Binomial Distribution**
- **Geometric and Negative Binomial Distribution**
- **The Poisson Distribution**
- **The Multinomial Distribution**

#### Continuous Distributions [see more](https://appliedmath.arizona.edu/sites/default/files/0f04d86a836182cbf608dfc86c7a70f5e5f6_0.pdf#%5B%7B%22num%22%3A179%2C%22gen%22%3A0%7D%2C%7B%22name%22%3A%22Fit%22%7D%5D)
- **Normal Distribution**
  - $f(x) = \frac{1}{\sigma \sqrt{2 \pi}} e^{-(x - \mu)^2/2\sigma^2}$
  - _The Lognormal Distribution_: the natural logarithm of a nonnegative random variable $V$ is normally distributed
- **Uniform Distribution**
  - $$\begin{split} f(x) = \left\{\begin{array}{ccc} \displaystyle \frac{1}{b-a} & , & a \le x \le b \\ 0 & , & \text{otherwise} \end{array} \right. \end{split}$$
  - $\mu = \frac{b+a}{2} \quad \sigma^2 = \frac{(b-a)^2}{12}$
- **Exponential Distribution**
  - $$\begin{split} f(x) = \left\{ \begin{array}{ccc} \lambda e^{- \lambda x} & , & x \ge 0 \\ 0 & , &  x < 0 \end{array} \right .\end{split}$$
  - $\mu = \frac{1}{\lambda} \quad \sigma^2 = \frac{1}{\lambda^2}$
- **Gamma Distribution**
  - $$\begin{split} f(x) = \left\{ \begin{array}{ccc} \displaystyle \frac{\beta^{\alpha}}{\Gamma(\alpha)} x^{\alpha - 1} e^{-\beta x}  & , & x \ge 0 \\ 0 & , & x < 0 \end{array} \right. \end{split}$$
  - $\mu = \frac{\alpha}{\beta} \quad \sigma^2 = \frac{\alpha}{\beta^2}$
- **Beta Distribution**
- **The Joint Normal Distribution**

### Random Sampling
- Scipy
  -  [`scipy.stats`](http://scipy-lectures.org/packages/statistics/index.html)

### Kernel Density Estimation
- [wikipedia](https://en.wikipedia.org/wiki/Kernel_density_estimation)
- [ubcmath](https://ubcmath.github.io/MATH360/stochastic/kernel.html)

## Examples
- [Stochastic Models, Statistics and Their Applications](https://link.springer.com/book/10.1007/978-3-319-13881-7)
  - professional and detailed
  - specific applications

