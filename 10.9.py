import matplotlib

import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(100, 50, 200)

plt.hist(x)
plt.show()