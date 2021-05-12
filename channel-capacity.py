# Sky Hoffert
# Strength of the Sun at distance.

import matplotlib.pyplot as plt
import numpy as np

f = 8e9
c = 3e8
wavelen = c / f

SNR = np.linspace(0, 40, 100)
BW = 1

C = BW * np.log2(1 + np.power(10, SNR/10))

D_earth_mars_farthest = 401e9 # m
D_earth_mars_average = 225e9 # m
D_earth_mars_closest = 54e9 # m
D_net = D_earth_mars_closest/2 # m

FSPL = np.power(4*np.pi*D_net / wavelen, 2)
FSPL_dB = 10 * np.log10(FSPL)

print(f"FSPL_dB = {FSPL_dB:.3f} dB")

v = np.where(np.isclose(SNR, 17, atol=0.1))
print(f"C[17 dB] = {C[v[0][0]]}")

plt.plot(SNR, C)
plt.title("Data Rate Relative to SNR")
plt.ylabel("Relative Bits per Hz (bits/Hz)")
plt.xlabel("SNR (dB)")
plt.show()
