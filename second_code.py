import matplotlib.pyplot as plt
import numpy as np

xrange = np.linspace(0, 20, 1000)

def f(x,a):
    func = a*np.exp(a*x)
    return func

plt.figure(dpi=256)
plt.plot(xrange, f(xrange, 5))
plt.yscale('log')
plt.xlabel("Time (s)")
plt.ylabel("Signal Amplitude")
plt.show()