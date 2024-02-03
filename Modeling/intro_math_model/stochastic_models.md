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
    - Purpose: Specify probability distributions for **continuous** variables
    - Characteristic: Area under the curve represents probability for an **interval**
  - **Probability Mass Functions** (PMFs)
    - Purpose: Describe probability distributions for **discrete** variables
    - Characteristic: Assigns probabilities to **specific values(points)**, not intervals
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

- **Bernoulli Distribution**
  - PMF: $P(X=k) = p^k(1-p)^{1-k}$ for $k \in \{0,1\}$
  - Mean: $\mu = p$
  - Variance: $\sigma^2 = p(1-p)$

- **Binomial Distribution**
  - PMF: $P(X=k) = \binom{n}{k}p^k(1-p)^{n-k}$ for $k = 0, 1, 2, ..., n$
  - Mean: $\mu = np$
  - Variance: $\sigma^2 = np(1-p)$

- **Geometric and Negative Binomial Distribution**
  - Geometric
    - PMF: $P(X=k) = (1-p)^{k-1}p$ for $k = 1, 2, 3, ...$
    - Mean: $\mu = \frac{1}{p}$
    - Variance: $\sigma^2 = \frac{1-p}{p^2}$
  - Negative Binomial
    - PMF: $P(X=k) = \binom{k-1}{r-1}p^r(1-p)^{k-r}$ for $k = r, r+1, r+2, ...$
    - Mean: $\mu = \frac{r}{p}$
    - Variance: $\sigma^2 = \frac{r(1-p)}{p^2}$

- **The Poisson Distribution**
  - PMF: $P(X=k) = \frac{e^{-\lambda}\lambda^k}{k!}$ for $k = 0, 1, 2, ...$
  - Mean: $\mu = \lambda$
  - Variance: $\sigma^2 = \lambda$

- **The Multinomial Distribution**
  - Probability Function: $P(X_1 = x_1, X_2 = x_2, ..., X_k = x_k) = \frac{n!}{x_1!x_2!...x_k!}p_1^{x_1}p_2^{x_2}...p_k^{x_k}$
  - Mean: $\mu_i = np_i$
  - Variance: $\sigma_i^2 = np_i(1-p_i)$
  - Covariance: $\text{Cov}(X_i, X_j) = -np_ip_j$ for $i \neq j$

#### Continuous Distributions [see more](https://appliedmath.arizona.edu/sites/default/files/0f04d86a836182cbf608dfc86c7a70f5e5f6_0.pdf#%5B%7B%22num%22%3A179%2C%22gen%22%3A0%7D%2C%7B%22name%22%3A%22Fit%22%7D%5D)

- **Normal Distribution**
  - PDF: $f(x) = \frac{1}{\sigma \sqrt{2 \pi}} e^{-(x - \mu)^2/2\sigma^2}$
  - _The Lognormal Distribution_: the natural logarithm of a nonnegative random variable $V$ is normally distributed

- **Uniform Distribution**
  - PDF:
    $$f(x) = \begin{cases}
        \frac{1}{b-a} & , a \le x \le b \\
        0 & , \text{otherwise}
      \end{cases}$$
  - Mean: $\mu = \frac{b+a}{2}$
  - Variance: $\sigma^2 = \frac{(b-a)^2}{12}$

- **Exponential Distribution**
  - PDF:
    $$f(x) = \begin{cases}
        \lambda e^{- \lambda x} & , x \ge 0 \\
        0 & , x < 0
      \end{cases}$$
  - Mean: $\mu = \frac{1}{\lambda}$
  - Variance: $\sigma^2 = \frac{1}{\lambda^2}$

- **Gamma Distribution**
  - PDF:
    $$f(x) = \begin{cases}
        \frac{\beta^{\alpha}}{\Gamma(\alpha)} x^{\alpha - 1} e^{-\beta x} & , x \ge 0 \\
        0 & , x < 0
      \end{cases}$$
  - Mean: $\mu = \frac{\alpha}{\beta}$
  - Variance: $\sigma^2 = \frac{\alpha}{\beta^2}$

- **Beta Distribution**
  - PDF: $f(x) = \frac{x^{\alpha-1}(1-x)^{\beta-1}}{B(\alpha,\beta)}$ for $0 < x < 1$
  - Mean: $\mu = \frac{\alpha}{\alpha + \beta}$
  - Variance: $\sigma^2 = \frac{\alpha\beta}{(\alpha + \beta)^2(\alpha + \beta + 1)}$

- **The Joint Normal Distribution**
  - PDF: $f(\mathbf{x}) = \frac{1}{\sqrt{(2\pi)^k|\Sigma|}} e^{-\frac{1}{2}(\mathbf{x}-\boldsymbol{\mu})^T\Sigma^{-1}(\mathbf{x}-\boldsymbol{\mu})}$
  - Here, $\mathbf{x}$ is a vector in $\mathbb{R}^k$, $\boldsymbol{\mu}$ is the mean vector, and $\Sigma$ is the covariance matrix.

##### Random Sampling

- Scipy
  - [`scipy.stats`](http://scipy-lectures.org/packages/statistics/index.html)

##### Kernel Density Estimation

- [wikipedia](https://en.wikipedia.org/wiki/Kernel_density_estimation)
- [ubcmath](https://ubcmath.github.io/MATH360/stochastic/kernel.html)
- [uw](https://faculty.washington.edu/yenchic/18W_425/Lec6_hist_KDE.pdf)
  
Kernel Density Estimation (KDE) Overview

- **Density Estimation**
  - Simple Estimation
    - Plotting histograms of observed random samples
- **Kernel Functions**
  - Functions \(K : \mathbb{R} \rightarrow \mathbb{R}\)
  - Examples: Triangular, Rectangular, Gaussian, Parabolic kernels
- **Kernel Density Functions**
  - Definition: \(\hat{f}_h(x) = \frac{1}{Nh} \sum \limits_{i=1}^N K \left( \frac{x - x_i}{h} \right)\)
  - Estimate of \(f(x)\)
  - Visualization: Impact of bandwidth on density estimation
- **KDE with SciPy**
  - `scipy.stats.gaussian_kde` function
    - Automates KDE computation with Gaussian kernel
  - Bandwidth parameter
    - Automatic or user-specified
    - Influences density estimation
  - Visualization

## Examples

- [Stochastic Models, Statistics and Their Applications](https://link.springer.com/book/10.1007/978-3-319-13881-7)
  - professional and detailed
  - specific applications
