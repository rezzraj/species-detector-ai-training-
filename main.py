from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

#  Load the data
iris = load_iris()
X = iris.data  # features (the 4 numbers)
y = iris.target  # labels (0,1,2)

#  Split data- 80% train, 20% test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#  Training model (K-Nearest Neighbors)
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

#  Predict & check accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f" Accuracy: {accuracy * 100:.2f}%")

#  Predict new input
example = [[5.1, 3.5, 1.4, 0.2]]  # you can change these numbers
predicted_class = model.predict(example)[0]
species = iris.target_names[predicted_class]
print(f"Predicted species: {species}")

