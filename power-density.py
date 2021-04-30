# Sky Hoffert
# Power density for distances.

import numpy as np
import matplotlib.pyplot as plt

c = 3e8 # m/s

D = 1e3 # m
f = 10e14 # Hz
wavelen = c/f # m
eff = 0.9**3

orbit_r = 1.87e11 # m (network orbit radius = 1.25 AU)
H_0 = 876 # W/m^2

G = 10 * np.log10(eff * (np.pi*D/wavelen)**2)
beamwid = 70 * wavelen / D

P_node = H_0 * np.pi * (D/2)**2
P_sent = P_node * eff

# power received is 50% because we are using half power beamwidth
P_rec = 0.5 * P_sent

print(f"f = {f:.3E} Hz")
print(f"D = {D:.3f} m")
print(f"eff = {eff:.3f}")
print(f"Gain = {G:.3f} dB")
print(f"Beamwidth = {beamwid:.9f} rad")

nNodesToCalc = 10
Ns = [10, 27, 40, 60]
PD_matrix = np.zeros([len(Ns), nNodesToCalc])

for i,N in enumerate(Ns):
    print(f"N = {N} Nodes")

    # This d calculation is an ESTIMATE, but close enough
    d = 2*np.pi*orbit_r / N

    r = d * np.tan(beamwid/2)
    D2 = 2*r

    print(f"  D2 = {D2:.3f} m")

    PD_rec = np.zeros([1,nNodesToCalc])
    PD_total = np.zeros([1,nNodesToCalc])

    PD_rec[0] = 0
    PD_total[0] = H_0

    print(f"  Node 1:")
    PD_rec[0][1] = (P_rec / (np.pi * (D2/2)**2))
    PD_total[0][1] = (PD_rec[0][1] + H_0)
    print(f"    PD = {PD_rec[0][1]:.3f} W/m^2")
    print(f"    PD (total) = {PD_total[0][1]:.3f} W/m^2")

    for n in range(2,nNodesToCalc):
        # PD_rec: Reflected + Focused
        # Reflected: 2 nodes ago * half power * efficiency of antenna
        # Focused: H_0 * efficiency of system * half power
        PD_rec[0][n] = (PD_rec[0][n-1] * 0.5 * eff + PD_rec[0][1])
        PD_total[0][n] = (PD_rec[0][n] + H_0)
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
plt.show()
