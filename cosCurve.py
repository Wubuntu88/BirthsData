#!/usr/bin/env python
import numpy as np
from scipy.optimize import curve_fit
from scipy.optimize import leastsq
import matplotlib.pyplot as plt
import math as math

'''
def cos_fit(x_value, b0, b1, b2):
    return b0 + b1 * np.cos(2 * np.pi * x_value / 1.0) + b2 * np.sin(2 * np.pi * x_value / 1.0)
'''


x = np.linspace(0, 4 * np.pi, 1000)
y = 3.0*np.sin(x + .00001) + 5.0  # + 0.5 + np.random.randn(1000)

guess_mean = np.mean(y)
guess_std = 3*np.std(y)/(2**0.5)
guess_phase = 0

data_first_guess = guess_std*np.sin(x+guess_phase) + guess_mean

#p is parameters
optFunc = lambda p: p[0]*np.sin(x+p[1]) + p[2] - y
guesses_for_params = [guess_mean, guess_std, guess_phase]
print guesses_for_params
est_std, est_phase, est_mean = leastsq(optFunc, guesses_for_params)[0]

y_fit = est_std * np.sin(x+est_phase) + est_mean

plt.plot(y, ".", c="red")  # plt.plot(x, y, ".")
plt.plot(y_fit, label='fit', c="green")
plt.plot(data_first_guess, label="guess", c="blue")
plt.legend()
plt.show()
'''
#y_fit = curve_fit(cos_fit, x, y)
optParams = y_fit[0]
print optParams

fitted_ys = []
for x_val in x:
    theY = cos_fit(x_val, optParams[0], optParams[1], optParams[2])
    fitted_ys.append(theY)

plt.plot(x, fitted_ys)
plt.scatter(x, y, c="green")
plt.show()
'''
