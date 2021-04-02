# Sky Hoffert
# Strength of the Sun at distance.

import matplotlib.pyplot as plt
import numpy as np

mdto = 3.7399e10 # m (mars distance to orbit = 0.25 AU)
r = 1.87e11 # m (network orbit radius = 1.25 AU)

N = 3 # number of nodes
while True:
    theta = 2*np.pi/N
    theta_deg = theta * 180/np.pi
    alpha = r * np.cos(theta/2)
    a = r - alpha
    d = 2 * (r * np.sin(theta/2))
    d2 = np.sqrt((d/2)**2 + (mdto+a)**2)
    print(f"theta={theta_deg:.3f} deg, alpha={alpha:.3E}")
    print(f"N={N}, d={d:.3E}, d2={d2:.3E}")
    print()
    N += 1
    if N > 10:
        break
