import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10, 0.1)
y = x * x
plt.plot(x, y)
plt.title('Example plots')
plt.xlabel('Input')
plt.ylabel('Function values')
plt.show()
