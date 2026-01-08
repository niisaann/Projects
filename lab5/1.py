import numpy as np
import matplotlib.pyplot as plt


x = np.array([1, 2, 3, 4, 5])
y = np.array([3, 5, 4, 7, 6])


x_mean = np.mean(x)
y_mean = np.mean(y)

beta1 = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean)**2)
beta0 = y_mean - beta1 * x_mean

print(f"Intercept (α): {beta0:.2f}")
print(f"Slope (β): {beta1:.2f}")

y_pred = beta0 + beta1 * x


plt.figure(figsize=(7,5))
plt.scatter(x, y, color='blue', label='Data points')
plt.plot(x, y_pred, color='red', label=f'Regression line: y = {beta0:.1f} + {beta1:.1f}x')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Simple Linear Regression')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.show()
