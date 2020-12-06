import numpy as np
import matplotlib.pyplot as plt
file="../PreVitamin_D/191125.txt"
hour,data=np.loadtxt(file,unpack=True)
plt.plot(hour,data)
plt.show()