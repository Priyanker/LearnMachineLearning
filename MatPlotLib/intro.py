import matplotlib.pyplot as plt

x = [1, 4, 9]
y = [1, 7, 5]

x2 = [1, 12]
y2 = [12, 1]


plt.plot(x, y, label='First Line')
plt.plot(x2, y2, label='Second Line')

# for dots at the point
plt.plot(x, y, 'o')
plt.plot(x2, y2, 'o')

plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('INTRO TO MATPLOTLIB')

plt.legend()
plt.show()
