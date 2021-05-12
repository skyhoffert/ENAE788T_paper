# Sky Hoffert
# Power density for distances.

import numpy as np
import matplotlib.pyplot as plt

c = 3e8 # m/s

def Clamp(v, min, max):
    if v < min:
        return min
    if v > max:
        return max
    return v

D = 1e3 # m
wavelen = 550e-9 # m
f = c/wavelen
eff_pointing = 0.2 # Depends on d
eff_reflector = 0.9
eff_wg = 0.9
eff_horn = 0.9
A = np.pi * (D/2)**2

orbit_r = 1.87e11 # m (network orbit radius = 1.25 AU)
H_0 = 876 # W/m^2

G = 10 * np.log10(eff_reflector * (np.pi*D/wavelen)**2)

print(f"f = {f:.3E} Hz")
print(f"wavelen = {wavelen:.3E} m")
print(f"D = {D:.3f} m")
print(f"Gain = {G:.3f} dB")

nNodesToCalc = 10
Ns = [10, 27, 40, 60, 80, 100]
PD_matrix = np.zeros([len(Ns), nNodesToCalc])

for i,N in enumerate(Ns):
    print(f"N = {N} Nodes")

    # This d calculation is an ESTIMATE, but close enough
    d = 2*np.pi*orbit_r / N
    tau_sq = A * A / (wavelen**2 * d**2)
    eta = 1 - np.exp(-tau_sq)

    eff_pointing = 1 - (d - 10e9) / (50e9)
    eff_pointing = Clamp(eff_pointing, 0.2, 0.95)

    print(f"  eta = {eta:.4f}")
    print(f"  eff_pointing = {eff_pointing:.4f}")

    PD_rec = np.zeros([1,nNodesToCalc])
    PD_total = np.zeros([1,nNodesToCalc])

    PD_rec[0][0] = 0
    PD_total[0][0] = H_0

    eff = eff_reflector * eff_wg * eff_horn * eff_pointing

    print(f"  Node 1:")
    PD_rec[0][1] = H_0 * eff * eta
    PD_total[0][1] = (PD_rec[0][1] + H_0)
    print(f"    PD = {PD_rec[0][1]:.3f} W/m^2")
    print(f"    PD (total) = {PD_total[0][1]:.3f} W/m^2")

    for n in range(2,nNodesToCalc):
        # PD_rec: Reflected + Focused
        # Reflected: 2 nodes ago * half power * efficiency of antenna
        # Focused: H_0 * efficiency of system * eta
        PD_rec[0][n] = PD_rec[0][n-1] * eff * eta + PD_rec[0][1]
        PD_total[0][n] = PD_rec[0][n] + H_0
        # print(f"Node {n}:")
        # print(f"  PD = {PD_rec[n]:.3f} W/m^2")
        # print(f"  PD (total) = {PD_total[n]:.3f} W/m^2")

    print(f"  Max PD = {np.max(PD_total):.3f} W/m^2")

    PD_matrix[i][:] = PD_total

for i,N in enumerate(Ns):
    plt.plot(PD_matrix[i][:])
plt.title("Network Power Chain")
plt.xlabel("Node Number")
plt.ylabel("Power Density (W/m^2)")
plt.annotate("N=10", [5, PD_matrix[0][5]+10])
plt.annotate("N=27", [5, PD_matrix[1][5]+10])
plt.annotate("N=40", [5, PD_matrix[2][5]+10])
plt.annotate("N=60", [5, PD_matrix[3][5]+25])
plt.annotate("N=80", [5, PD_matrix[4][5]+50])
plt.annotate("N=100", [5, PD_matrix[5][5]+100])
plt.show()
