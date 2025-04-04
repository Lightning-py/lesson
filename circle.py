import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 100) 

y_upper = np.sqrt(4 - x**2) 
y_lower = -1 * np.sqrt(4 - x**2)  

plt.plot(x, y_upper, label='y = +sqrt(4 - x^2)', color='blue')
plt.plot(x, y_lower, label='y = -sqrt(4 - x^2)', color='red')

# plt.title('y = +-sqrt(4 - x^2)')  

# plt.xlabel('x')
# plt.ylabel('y')

# plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.axis('equal')
# plt.legend()

plt.show()
