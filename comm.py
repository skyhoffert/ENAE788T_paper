
import numpy as np

c = 3e8

D = 1e3 # m
f = 8e9 # Hz
wavelen = c/f

A = np.pi * (D/2)**2

G = 4*np.pi*A/wavelen**2 * 0.8
G_dB = 10 * np.log10(G)

print(f"D = {D:.4f} m")
print(f"G = {G_dB:.2f} dB")
print()

D = 70 # m
A = np.pi * (D/2)**2
G = 4*np.pi*A/wavelen**2 * 0.8
G_dB = 10 * np.log10(G)

print(f"D = {D:.4f} m")
print(f"G = {G_dB:.2f} dB")
print()
