# Deterministic Models

## Overview

- **deterministic**: always produces the same output for the same initial conditions
- Often formulated as _systems of differential equations_
  - applying **physical laws** to get the functions
  - applying the **nondimensionalization** procedure
    - scale the model variables to simply the model
    - provide insight into the system’s behavior in terms of the parameters
  - solving:
    - analytically solvable (if lucky), use mathematica etc.
    - approximate with _numerical methods_, use **Scipy** etc.

## Differential Equations

### analytical methods

...

- mathematica

### numerical methods [\ref](https://pythonnumericalmethods.berkeley.edu/notebooks/chapter22.00-ODE-Initial-Value-Problems.html)

- [Euler's method](https://pythonnumericalmethods.berkeley.edu/notebooks/chapter22.03-The-Euler-Method.html)
- [RK method](https://pythonnumericalmethods.berkeley.edu/notebooks/chapter22.05-Predictor-Corrector-Methods.html)
- Scipy
  - [`scipy.integrate.odeint`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.odeint.html)
  - [`scipy.integrate.solve_ivp`](https://pythonnumericalmethods.berkeley.edu/notebooks/chapter22.06-Python-ODE-Solvers.html)
  - [`scipy.integrate.solve_bvp`](https://pythonnumericalmethods.berkeley.edu/notebooks/chapter23.05-Python-ODE-Solvers.html)

- How to use `scipy` to solve IVP
  1. Judge whether one dimension, first order
  2. For higher order problem, convert to multi-dimension problem
  3. Solve one dimension problem or multi-dimension problem
  4. Plot the result

### Nondimensionalization

- **dimension** of a [physical quantity](https://en.wikipedia.org/wiki/International_System_of_Quantities) refers to its expression in terms of the _base quantities_, such as time, length, mass and temperature.
- An equation is **dimensionally homogeneous** if the expressions on both sides of the equation have the same dimensions.
- **Nondimensionalization**: scaling variables to simplify the model and identify the key properties in terms of _dimensionless parameters_.
  - [example](https://ubcmath.github.io/MATH360/deterministic/nondimensionalization/scaling.html)

## Examples

- [Objectes in Motion](https://ubcmath.github.io/MATH360/deterministic/motion/index.html)
- [Heat Transfer](https://ubcmath.github.io/MATH360/deterministic/heat/index.html)
- [Mass Balance](https://ubcmath.github.io/MATH360/deterministic/heat/index.html)
