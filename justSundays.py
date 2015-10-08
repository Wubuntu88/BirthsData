#!/usr/bin/env python
__author__ = 'will'
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from scipy import *
from scipy.optimize import leastsq


x = [1, 8, 15, 22, 29, 36, 43, 50, 57, 64, 71, 78, 85, 92, 99, 106, 113, 120, 127, 134, 141, 148, 155, 162, 169, 176, 183, 190, 197, 204, 211, 218, 225, 232, 239, 246, 253, 260, 267, 274, 281, 288, 295, 302, 309, 316, 323, 330, 337, 344, 351, 358]
x = np.array(x)
y =[7701.0, 7611.0, 7771.0, 7560.0, 7527.0, 7804.0, 7950.0, 7695.0, 7881.0, 7791.0, 7870.0, 7729.0, 7589.0, 7691.0, 7445.0, 7193.0, 7304.0, 7135.0, 7388.0, 7382.0, 7570.0, 7781.0, 7399.0, 7581.0, 7777.0, 8091.0, 7976.0, 8102.0, 8416.0, 8563.0, 8486.0, 8442.0, 8532.0, 8477.0, 8453.0, 8355.0, 8630.0, 8711.0, 8647.0, 8686.0, 8377.0, 7873.0, 7936.0, 8155.0, 8011.0, 7967.0, 7868.0, 8068.0, 8196.0, 8093.0, 8172.0, 7964.0]
y = np.array(y)
sinx = np.sin(2*np.pi*x/365.0)
cosx = np.cos(2*np.pi*x/365.0)

guess_mean = np.mean(y)
guess_std = 100*np.std(y)/(2**0.5)
guess_phase = 0

guesses_for_params = [guess_mean, guess_std, guess_phase]

optFunc = lambda p: p[0] + p[1]*sinx + p[2]*cosx - y
result = leastsq(optFunc, [1, 1, 1])
coeffs = result[0]
y_fit = coeffs[0] + coeffs[1]*sinx + coeffs[2]*cosx

print "eq:" + str(coeffs[0]) + " " + str(coeffs[1]) + "*sin(x) + " + str(coeffs[2]) + "*cos(x)"

plt.scatter(x, y, marker="o", s=40)
plt.plot(x, y_fit, label="fit", c="green", linewidth=1)
plt.show()
