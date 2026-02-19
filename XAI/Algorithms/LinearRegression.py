import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Example data: [Square Footage, Number of Bedrooms]
X = np.array([[1500, 3], [2000, 4], [2500, 4], [3000, 5]])
y = np.array([300000, 400000, 500000, 600000])

lin_reg = LinearRegression()
lin_reg.fit(X,y)

# Output the intercept and coefficients
print("Intercept:", lin_reg.intercept_)
print("Coefficients:", lin_reg.coef_)

# Predict house prices using the trained model
y_pred = lin_reg.predict(X)
print("Predicted Prices:", y_pred)