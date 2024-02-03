import matplotlib.pyplot as plt
from numpy import sin, linspace
from scipy.integrate import solve_ivp

# INFO: Demo for one dimension, first order


def f_1(t, y):
    """
    dy/dt=f1(y,t)=sin(t^2)
    """
    return sin(t**2)


def sol_first_order():
    """
    one dimension, first order
    """
    t1 = linspace(-10, 10, 1000)
    y0 = [10]

    ret = solve_ivp(fun=f_1, t_span=(-10, 10), y0=y0, t_eval=t1)

    plt.plot(ret.t, ret.y[0])
    plt.show()


# INFO: Demo for one dimension, second order


def f_2(t, Y):
    """
    y''=-y'^2+sin(y)
    Y=[y,y']
    """
    y, v = Y
    return [v, -(v**2) + sin(y)]  # dy/dt=v  dv/dt=-v**2+sin(y)


def sol_sys():
    """
    solve differential equation system
    """
    y0 = 0
    v0 = 3
    Y0 = (y0, v0)
    t = linspace(0, 1, 100)

    ret = solve_ivp(fun=f_2, t_span=(0, 1), y0=Y0, t_eval=t)

    plt.plot(ret.t, ret.y[0])
    plt.show()


# sol_first_order()
# sol_sys()
