import matplotlib.pyplot as plt
import numpy as np
x = np.array(["Node.js", "Python", "Java", "PHP"])
y = np.array([10, 9, 7, 5])
plt.bar(x, y, color = "#4CAF50", width = 0.5)
plt.show()