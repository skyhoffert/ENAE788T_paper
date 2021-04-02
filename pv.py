# Sky Hoffert
# Strength of the Sun at distance.

import matplotlib.pyplot as plt
import numpy as np

# Mercury, Venus, Earth, Mars, Asteroids, Jupiter, Saturn, Uranus, Neptune
# D = np.array([57.909e9, 108.209e9, 149.6e9, 227.923e9, 389e9, 778.570e9, \
    # 1427e9, 2870e9, 4498e9]) # m
D = np.linspace(50e9, 400e9, 100) # m

D_earth = 149.6e9 # m
D_mars = 227.9e9 # m
D_neptune = 4.488e12 # m

H_sun = 64e6 # W/m^2
R_sun = 695e6 # m

earth_idx = -1
mars_idx = -1
neptune_idx = -1

H_0 = np.zeros(len(D))
for i,d in enumerate(D):
    H_0[i] = R_sun**2 / d**2 * H_sun
    if d <= D_earth:
        earth_idx = i
    if d <= D_mars:
        mars_idx = i
    if d <= D_neptune:
        neptune_idx = i

plt.plot(D, H_0)
plt.title("Solar Energy at Distance")
plt.xlabel("Distance from Sun (m)")
plt.ylabel("Energy Density (W/m^2)")
plt.axvline(x=D_earth, color='g', linestyle=':')
plt.axvline(x=D_mars, color='r', linestyle=':')
plt.annotate("Earth", [D_earth, H_0[earth_idx]], \
    [D_earth+25e9, H_0[earth_idx]+1200], \
    arrowprops=dict(facecolor="black", width=1, headwidth=6, headlength=8, \
    shrink=0.15))
plt.annotate("Mars", [D_mars, H_0[mars_idx]], \
    [D_mars+25e9, H_0[mars_idx]+1200],\
    arrowprops=dict(facecolor="black", width=1, headwidth=6, headlength=8, \
    shrink=0.15))
plt.show()

print(f"H_0 at Earth = {H_0[earth_idx]:.3f} W/m^2")
print(f"H_0 at Mars = {H_0[mars_idx]:.3f} W/m^2")
print(f"H_0 at Neptune = {H_0[neptune_idx]:.3f} W/m^2")
