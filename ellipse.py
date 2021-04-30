# Sky Hoffert
# Used to find angle that an ellipse will appear as a circle.

import numpy as np

a = 1
b = 8

theta = np.arccos(a / b)

# For 27 nodes, we want each node to have
# ((N-2)*180 / N) / 2 angle
# this requires b/a of 8

print(f"b/a = {b/a:.3f}")
print(f"theta = {theta*180/np.pi:.3f} deg")
