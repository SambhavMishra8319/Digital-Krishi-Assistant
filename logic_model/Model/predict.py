import joblib
import sys
import os

print(sys.executable)

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def predict_crop(N, P, K, ph, temp, humidity, rain, city_name):
    # Load the trained model and label encoder
    model = joblib.load("Model/crop_model.pkl")
    le = joblib.load("Model/label_encoder.pkl")

    # Prepare feature list in correct order
    features = [N, P, K, temp, humidity, ph, rain]

    # Make prediction
    prediction = model.predict([features])[0]
    crop_name = le.inverse_transform([prediction])[0]
    return crop_name

if __name__ == "__main__":
    print("Recommended Crop:", predict_crop(25, 56,84, 45, 82, 6.5, 225, "Pune"))
