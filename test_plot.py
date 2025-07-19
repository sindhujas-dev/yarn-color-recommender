import matplotlib
matplotlib.use("TkAgg")  # Or try "QtAgg" if this doesn't work

import matplotlib.pyplot as plt

# Basic plot
plt.plot([1, 2, 3], [4, 5, 6])
plt.title("Matplotlib Test")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
