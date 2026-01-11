import matplotlib.pyplot as plt
import numpy as np


species = (
    "Adelie",
    "Chinstrap",
    "Gentoo",
)
weight_counts = {
    "Below": np.array([70, 31, 58]),
    "Above": np.array([82, 37, 66]),
}
width = 0.5

fig, ax = plt.subplots()
bottom = np.zeros(3)

for boolean, weight_count in weight_counts.items():
    p = ax.bar(species, weight_count, width, label=boolean, bottom=bottom)
    bottom += weight_count

ax.legend(loc="upper right")

plt.show()