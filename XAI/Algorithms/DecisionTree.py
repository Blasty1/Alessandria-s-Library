import matplotlib.pyplot as plt
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

X, y = make_classification(
   n_samples=100, # Number of samples
   n_features=3, # Number of features
   n_informative=3, # Number of informative features
   n_redundant=0, # No redundant features
   n_classes=2, # Binary classification
   random_state=42 # Random seed for reproducibility
)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
    random_state=42)

clf = DecisionTreeClassifier(max_depth=4, random_state=42)
clf.fit(X_train,y_train)

# 4. Extract the feature importance scores from the trained classifier
feature_importances = clf.feature_importances_

features = np.array(["Feature 1", "Feature 2", "Feature 3"])

plt.barh(features,feature_importances)
plt.xlabel("Importance Score") # Label for the x-axis
plt.title("Feature Importance in Decision Tree") # Title of the plot
plt.show() # Display the plot