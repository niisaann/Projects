import numpy as np
import matplotlib.pyplot as plt

# Data
x = np.array([1, 2, 3, 4, 5])
y = np.array([3, 5, 4, 7, 6])

# Means
x_mean = np.mean(x)
y_mean = np.mean(y)

# Regression coefficients
beta1 = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean)**2)
beta0 = y_mean - beta1 * x_mean

# Predicted values
y_pred = beta0 + beta1 * x

# Residuals = actual - predicted
residuals = y - y_pred

print("Residuals:", np.round(residuals, 2))

# Plot residuals
plt.figure(figsize=(7,5))
plt.scatter(x, residuals, color='purple', label='Residuals')
plt.axhline(0, color='black', linestyle='--', linewidth=1)
plt.xlabel('x')
plt.ylabel('Residual (y - ŷ)')
plt.title('Residual Plot')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.show()
