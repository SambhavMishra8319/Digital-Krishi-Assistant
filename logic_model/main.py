from Model.train_model import train_model
from Model.predict import predict_crop_with_weather

if __name__ == "__main__":
    # Step 1: Train the model
    train_model()

    # Give input to the model
    try:
        N = float(input("Enter Nitrogen value (N): "))
        P = float(input("Enter Phosphorus value (P): "))
        K = float(input("Enter Potassium value (K): "))
        ph = float(input("Enter soil pH: "))
        city = input("Enter your city name: ")

        # Step 3: Predict crop
        recommended_crop = predict_crop_with_weather(N, P, K, ph, city)

        print(f"\n✅ Recommended Crop for {city}: {recommended_crop}")

    except ValueError:
        print("❌ Please enter valid numeric values for N, P, K, and pH.")