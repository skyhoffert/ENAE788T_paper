# Sky Hoffert
# Power density for distances.

import numpy as np
import matplotlib.pyplot as plt

c = 3e8 # m/s

D = 1e3 # m
f = 10e14 # Hz
wavelen = c/f # m
eff = 0.8

d = 43.42e9 # m

H_0 = 876 # W/m^2

P_node = H_0 * np.pi * (D/2)**2
P_sent = P_node * eff

# power received is 50% because we are using half power beamwidth
P_rec = 0.5 * P_sent

G = 10 * np.log10(eff * (np.pi*D/wavelen)**2)
beamwid = 70 * wavelen / D

print(f"f = {f:.3E} Hz")
print(f"D = {D:.3f} m")
print(f"eff = {eff:.3f}")
print(f"Gain = {G:.3f} dB")
print(f"Beamwidth = {beamwid:.9f} rad")

r = d * np.tan(beamwid/2)
D2 = 2*r

print(f"D2 = {D2:.3f} m")

PD_rec = P_rec / (np.pi * (D2/2)**2)
print(f"PD = {PD_rec:.3f} W/m^2")

orb_r = 1.87e11 # m (network orbit radius = 1.25 AU)
sep = d
N = 2*np.pi*orb_r / sep
print(f"Num Nodes = {N:.3f}")
