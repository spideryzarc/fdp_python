import numpy as np

def f(a):
    return 5+ 3*np.sin(a)

a = np.linspace(0, 2*np.pi, 100)
print(a)

r = f(a)
# convertendo para cartesiano
x = r*np.cos(a)
y = r*np.sin(a)

import matplotlib.pyplot as plt
plt.plot(x, y)
plt.show()


