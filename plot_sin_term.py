"""
Plot sin_term = sin(180° / N) for integer N.
Used in resonant orbit calculations (e.g. SMA formula).
"""

import math
import matplotlib.pyplot as plt

# Integer N values to evaluate (N >= 2 for meaningful angles)
N_MIN = 2
N_MAX = 50
n_values = list(range(N_MIN, N_MAX + 1))

sin_terms = [math.sin(math.radians(180 / n)) for n in n_values]

fig, ax = plt.subplots()
ax.plot(n_values, sin_terms, "o-", markersize=4)

ax.set_xlabel("N (number of satellites)")
ax.set_ylabel("sin(180° / N)")
ax.set_title("sin_term for integer N")
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("sin_term_plot.png", dpi=150)
plt.show()
