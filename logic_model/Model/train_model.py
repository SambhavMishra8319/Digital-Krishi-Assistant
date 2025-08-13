from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
from Model.dataset_load import load_data  # <-- make sure dataset_load.py exists

def train_model():
    # Load data
    X, y, le = load_data()

    # Split into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Create & train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Predictions & evaluation
    y_pred = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred, target_names=le.classes_))

    # Save model & label encoder
    joblib.dump(model, "Model/crop_model.pkl")
    joblib.dump(le, "Model/label_encoder.pkl")

# This just runs the training if we run the file directly
if __name__ == "__main__":
    train_model()
