import pandas as pd
from sklearn.model_selection import KFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv('Dataset/Crop_recommendation.csv')

# Separate features and target
X = data.drop('label', axis=1)
y = data['label']

# Prepare KFold with 5 splits
kf = KFold(n_splits=5, shuffle=True, random_state=42)

accuracies = []

for train_index, test_index in kf.split(X):
    X_train, X_test = X.iloc[train_index], X.iloc[test_index]
    y_train, y_test = y.iloc[train_index], y.iloc[test_index]

    # Initialize and train model
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Predict on test fold
    y_pred = model.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    accuracies.append(accuracy)

# Average accuracy across folds
average_accuracy = sum(accuracies) / len(accuracies)
print(f'Average Cross-Validated Accuracy: {average_accuracy:.4f}')
