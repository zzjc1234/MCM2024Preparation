from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


def f_1(t, y):
    """
    one dimension, first order
    ADD YOUR EXPRESSION HERE
    """
    dy = 111  # INFO: replace 111 with expression
    return dy


def f_multi(t, Y):
    """
    multi dimension first order or
    one dimension higher order
    """
    # INFO: template for multi dimension problem
    # v0=Y[0]
    # v1=Y[1]
    # v2=Y[2]
    # ...
    # return EXPRESSION

    # INFO: template for higher order ode
    # y'=Y[1]
    # y''=Y[2]
    # y(n)=Y[n]
    # ...
    # return [y', y'', ... , EXPRESSION]
    pass


def ode(func, t_span, y0, t_eval):
    """
    one dimension, first order ode
    """

    ret = solve_ivp(fun=func, t_span=t_span, y0=y0, t_eval=t_eval)
    plt.plot(ret.t, ret.y)
    plt.show()


def ode_sys(func, t_span, Y0, t_eval):
    """
    solve differential equation system
    """

    ret = solve_ivp(fun=func, t_span=t_span, y0=Y0, t_eval=t_eval)
    plt.plot(ret.t, ret.y[0])
    plt.show()
