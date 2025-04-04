import numpy as np
import matplotlib.pyplot as plt


data = np.random.randn(1000) 


plt.hist(data, bins=30, color='blue', alpha=0.7, edgecolor='black') 


plt.title('Гистограмма случайных данных')  
plt.xlabel('Значения')  
plt.ylabel('Частота')  
plt.grid(axis='y', alpha=0.75) 

plt.show()
