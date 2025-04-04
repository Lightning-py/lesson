import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2 * np.pi, 100) 

x = 2 * np.cos(theta)
y = 2 * np.sin(theta)  


plt.plot(x, y, label='x^2 + y^2 = 4', color='blue')


plt.xlabel('x')  
plt.ylabel('y')  
plt.grid(color='gray', linestyle='--', linewidth=0.5)  
plt.axis('equal')  
plt.legend()


plt.show()