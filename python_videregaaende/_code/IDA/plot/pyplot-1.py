# pip3 install PyQt5
# https://pypi.org/project/PyQt5/

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)

# Vis plot
plt.show()

# Gem plot
plt.savefig('demoplot.png')