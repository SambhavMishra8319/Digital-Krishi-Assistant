from Model.train_model import train_model
from Model.weather_fetch import get_weather
from Model.predict import predict_crop
from Model.soil_predict import get_soil_values_by_city

if __name__ == "__main__":
    # Step 1: Train the model
    train_model()

    # Give input to the model
    try:
        city = input("Enter your city name: ")

        #Predict Soil data and weather
        N, P, K, ph = get_soil_values_by_city(city)
        temp, humidity, rain = get_weather(city)

        # Step 3: Predict crop
        recommended_crop = predict_crop(N, P, K, temp, humidity, ph, rain, city)

        print(f"\n Recommended Crop for {city}: {recommended_crop}")

    except ValueError:
        print(" There is a error in predicting the crop or predicting the soil information!!!")