import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 10, 100)
y = np.sqrt(x)

x2 = np.linspace(-1, 1, 10)
y2 = np.sin(x2)

print(x)
print(y)

# первый график
plt.subplot(1, 2, 1)

plt.title('Кековый график функции')  
plt.plot(x, y, label='y = sqrt(x)', color='blue', marker='|')
plt.plot(0, 0, marker='o', markersize=10)

# второй график
plt.subplot(1, 2, 2)

plt.plot(x2, y2, label='синус', color='red')

plt.xlabel('Ахахаха') 
plt.ylabel('Лол кек') 

plt.legend()

plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5) 

plt.subplot(1, 3, 3)

plt.pie([15, 30, 45], labels=['было два козла', 'сколько', 'на размышление дается'])

plt.show()
