from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix

# Simple dataset: [height, Weight]
X = [
    [150,50],
    [160,60],
    [170,65],
    [180,80]
]
# Labels: 0 = Short , 1 = Tall
y = [0,0,1,1]

# Create and train the model
model = DecisionTreeClassifier()
model.fit (X,y)

# Predict for the same data (for destination)
y_pred = model.predict(X)

# Compute confusion matrix
cm = confusion_matrix(y,y_pred)
print("Confusion Matrix:")
print(cm)