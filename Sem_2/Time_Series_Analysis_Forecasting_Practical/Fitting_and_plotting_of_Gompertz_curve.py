import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def gompertz(x, a, b, c):
    return a * np.exp(-b * np.exp(-c * x))

x = np.linspace(0, 10, 50)
y = 5 * np.exp(-2 * np.exp(-0.8 * x)) + 0.1 * np.random.randn(len(x))

popt, _ = curve_fit(gompertz, x, y)

x_smooth = np.linspace(0, 10, 200)
y_fit = gompertz(x_smooth, *popt)

plt.scatter(x, y, label="Actual Data", color="red")
plt.plot(x_smooth, y_fit, label="Fitted Gompertz Curve", linewidth=2)

plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Fitting and Plotting Gompertz Curve")
plt.legend()
plt.grid(True)
plt.show()