1. The Primal Approach:
   The primal approach is based on the Cobb-Douglas production function, augmented to include knowledge capital. The log-linear form of the estimation equation would be:

   \[\Delta y_{it} = \lambda_t + \alpha \Delta l_{it} + \beta \Delta c_{it} + \gamma \Delta k_{it} + \phi \Delta k_{ot} + \Delta u_{it}\]

   where:
   - \(\Delta y_{it}\) is the change in output,
   - \(\Delta l_{it}\) is the change in labor input,
   - \(\Delta c_{it}\) is the change in physical capital,
   - \(\Delta k_{it}\) is the change in the firm's own R&D capital,
   - \(\Delta k_{ot}\) is the change in the stock of external knowledge,
   - and \(\Delta u_{it}\) is the change in utilization or efficiency.

   The parameters \(\gamma\) and \(\phi\) represent the output elasticities with respect to the firm's own R&D capital and to external R&D capital, respectively.

2. The Dual Approach:
   The dual approach utilizes a variable cost function and factor demand equations. For example, in a simplified translog cost function, the equation may look like:

   \[ln(C) = \alpha_0 + \alpha_l ln(L) + \alpha_c ln(Cap) + \alpha_k ln(K) + \frac{1}{2}[ \alpha_{ll}(ln(L))^2 + \alpha_{cc}(ln(Cap))^2 + \alpha_{kk}(ln(K))^2]\]

   where:
   - \(C\) represents the total variable cost,
   - \(L\) represents labor,
   - \(Cap\) represents physical capital,
   - \(K\) represents R&D capital,
   - with respective coefficients \(\alpha\) and half the squares for interaction terms denoted by \(\alpha_{ll}\), \(\alpha_{cc}\), \(\alpha_{kk}\).

This summarizes the key equations used in the paper within the production function framework for estimating the returns to R&D investments.

Yes, based on the aforementioned formulas, the valuation of a patent, both its present and expected future value, can be summarized in the following formula:

**Net Present Value (NPV) of a Patent:**

\[ NPV = \sum_{t=0}^{T} \frac{(r(t) - c(t))}{(1 + i)^t} \]

Where:

- \( t \) is the current time period from the granting of the patent up to the patent's maximum lifespan (T),
- \( r(t) \) is the return from the patent at time \( t \),
- \( c(t) \) is the renewal cost of the patent at time \( t \),
- \( i \) is the discount rate reflecting the time value of money,
- \( NPV \) is the net present value of the patent over its lifespan.

To unpack this formula:

1. **Return \( r(t) \) at Time \( t \):**

\[ r(t) = r(0)e^{(-dt)} \]

- \( r(0) \) is the initial return at the time of application / filing the patent,
- \( e \) is the base of the natural logarithm,
- \( d \) is the depreciation rate of the patent returns over time.

2. **Present Value of Profits Factor \( z(t) \):**

\[ z(t) = \frac{e^{(-st)}}{d + s} [1 - e^{(-s)}] \]

- \( s \) is the discount rate,
- Exponential terms reflect the present value of future profits, discounted back to the present time.

3. **Initial Return Distribution:**

\[ \ln(r(0)) = \beta \cdot X + \varepsilon \]

- Where \( X \) is the vector of patent characteristics,
- \( \beta \) is the coefficient vector indicating the influence of \( X \) on the initial return,
- \( \varepsilon \) is a normally distributed random variable representing uncertainty.

The NPV formula integrates the return profiles over the patent's potential life considering the opportunity costs (renewal fees) and the time value of money via discounting. This theoretical construct allows for the estimation of the patent's value both currently and in the future, accommodating for the decline in returns and costs associated with maintaining the patent.

The method, while broadly applicable, would still need to be adjusted for specific patents' characteristics, market conditions, and other factors that may affect the utility and exploitative potential of the patent at various points in its life.
