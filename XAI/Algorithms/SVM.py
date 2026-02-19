import numpy as np
from sklearn import datasets
from sklearn.svm import SVC
import matplotlib.pyplot as plt

# Load a sample dataset with two features
X, y = datasets.make_classification(n_samples=100, n_features=2,
                           n_informative=2, n_redundant=0, n_repeated=0,
                           n_classes=2, n_clusters_per_class=1,
                           random_state=42)

model = SVC(kernel="linear")
model.fit(X,y)

w = model.coef_[0]
b = model.intercept_[0]

# Define the decision boundary
x_points = np.linspace(min(X[:, 0]), max(X[:, 0]), 100)
y_points = -(w[0] / w[1]) * x_points - b / w[1]
# w x = 0
# [w_0, w_1] [x_0 , x_1]^T + b = 0
# w_0 x_0 + w_1 x_1 + b = 0
# x_1 = -b/w_1 - w_0/w_1 x_0

# Plot the data points and decision boundary
plt.scatter(X[:, 0], X[:, 1], c=y, cmap="coolwarm", edgecolors="k", label="Data Points")
plt.plot(x_points, y_points, color="red", label="Decision Boundary")
# Highlight the support vectors
plt.scatter(model.support_vectors_[:, 0], model.support_vectors_[:, 1],
         s=100, facecolors="none", edgecolors="k", linewidths=1.5,
         label="Support Vectors")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("SVM Decision Boundary with Support Vectors")
plt.legend()
plt.show()