# Sky Hoffert
# Experimenting with configurations of solar orbit satellites.

import math

###################################################################################################
print("Section 1: Orbit between Earth and Mars.")
###################################################################################################

R_earth = 160.876e9 # m
R_mars = 226.9e9 # m
R_NET = 193.89e9 # m

max_sep = R_earth + R_mars
avg_sep = R_mars
min_sep = R_mars - R_earth

diam_MRO = 0.45 # m
diam_DSN = 70 # m
diam_NET = 0.5 # m

f = 8.44e9 # Hz
wavelen = 3e8 / f # m
pi = 3.1415926

A_t = pi * (diam_MRO/2)**2 # m^2
A_r = pi * (diam_DSN/2)**2 # m^2

L_max = 10 * math.log10((A_r * A_t) / ((max_sep)**2 * (wavelen)**2))
L_avg = 10 * math.log10((A_r * A_t) / ((avg_sep)**2 * (wavelen)**2))
L_min = 10 * math.log10((A_r * A_t) / ((min_sep)**2 * (wavelen)**2))

print("DSN connection has:")
print(f"  L_max = {L_max:.1f} dB")
print(f"  L_avg = {L_avg:.1f} dB")
print(f"  L_min = {L_min:.1f} dB")

net_sep = min_sep/2
num_net = math.ceil(2*pi*R_NET / net_sep)

print()
print(f"Assuming separation between net sats is {net_sep/1e9:.3f} Gm")
print(f"This requires {num_net} net satellites.")
print()

L_net = L_avg
diam_net = 2 * math.sqrt(wavelen**2 * net_sep**2 * 10**(L_net/10) / (A_t * pi))

print("In order to meet average DSN performance:")
print(f"  diam_net = {diam_net:.2f} m")

L_net = L_min
diam_net = 2 * math.sqrt(wavelen**2 * net_sep**2 * 10**(L_net/10) / (A_t * pi))

print("In order to meet best DSN performance:")
print(f"  diam_net = {diam_net:.2f} m")
