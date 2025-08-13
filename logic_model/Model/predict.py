import joblib
from Model.weather_fetch import get_weather  # correct import

def predict_crop_with_weather(N, P, K, ph, city_name):
    # Load the trained model and label encoder
    model = joblib.load("Model/crop_model.pkl")
    le = joblib.load("Model/label_encoder.pkl")

    # Get live weather data
    temp, humidity, rain = get_weather(city_name)

    # Prepare feature list in correct order
    features = [N, P, K, temp, humidity, ph, rain]

    # Make prediction
    prediction = model.predict([features])[0]
    crop_name = le.inverse_transform([prediction])[0]
    return crop_name

if __name__ == "__main__":
    print("Recommended Crop:", predict_crop_with_weather(90, 42, 43, 6.5, "Pune"))
