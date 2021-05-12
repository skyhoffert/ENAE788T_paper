# Sky

from statistics import NormalDist

import numpy as np

r_r = 500 # m
r_t = 500 # m
wavelen = 2e-5 # m
d = 43.42e9 # m

A_r = np.pi*r_r**2
A_t = np.pi*r_t**2

tau = A_t * A_r / (wavelen**2 * d**2)
eta = 1 - np.exp(-tau**2)

print(f"tau = {tau:.6f}")
print(f"eta = {eta:.6f}")

v = NormalDist().cdf(2)
print(f"v = {v:.3f}")
