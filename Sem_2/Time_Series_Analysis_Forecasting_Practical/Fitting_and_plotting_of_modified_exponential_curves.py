import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def modified_exp(x, a, b, c):
    return a * (1 - np.exp(-b * x)) + c

x = np.linspace(0, 10, 50)
y = 3*(1 - np.exp(-0.7*x)) + 2 + 0.2*np.random.randn(len(x)) 

popt, _ = curve_fit(modified_exp, x, y)

x_smooth = np.linspace(0, 10, 200)
y_fit = modified_exp(x_smooth, *popt)

plt.scatter(x, y, label="Data")
plt.plot(x_smooth, y_fit, label="Fitted Modified Exponential Curve")#Line plot → the fitted curve
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()