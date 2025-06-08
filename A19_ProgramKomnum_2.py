import numpy as np
from sympy import *

def error_true(y_real, x_n):
    return abs((y_real - x_n) / y_real)

def error_aprox(x_n, x0):
    return abs((x_n - x0) / x_n) if x_n !=0 else float('inf')

def f(x):
    return x**3 + x**2 - 34*x - 56 

def bisection(xl, xu, x_true, max_iter=3, tol=1e-5):
    print(f"{'Iter':<5}{'XL':<10}{'XU':<10}{'XR':<10}{'f(XR)':<12}{'ε_t (%)':<10}{'ε_a (%)':<10}")
    print("-" * 65)

    xr_old = None
    for i in range(1, max_iter+1):
        xr = (xl + xu) / 2
        f_xr = f(xr)
        
        et = abs((x_true - xr) / x_true) * 100
        
        ea = abs((xr - xr_old) / xr) * 100 if xr_old is not None else None
        
        ea_str = f"{ea:.2f}" if ea is not None else "-"
        print(f"{i:<5}{xl:<10.2f}{xu:<10.2f}{xr:<10.2f}{f_xr:<12.2f}{et:<10.2f}{ea_str:<10}")
        
        if ea is not None and ea < tol:
            break

        if f(xl) * f_xr < 0:
            xu = xr
        else:
            xl = xr

        xr_old = xr

bisection(xl = -2, xu = 3, x_true=2)
