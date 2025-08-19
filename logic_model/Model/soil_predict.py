import pandas as pd

# Load the soil dataset once
soil_df = pd.read_csv('Dataset/Citywise_soildata_100.csv')

def get_soil_values_by_city(city_name):
    # Lookup city name (case-insensitive)
    record = soil_df[soil_df['city'].str.lower() == city_name.lower()]
    
    if record.empty:
        raise ValueError(f"Soil data not found for city: {city_name}")
    
    # Access soil parameters from the first matching record
    N = float(record.iloc[0]['N'])
    P = float(record.iloc[0]['P'])
    K = float(record.iloc[0]['K'])
    ph = float(record.iloc[0]['ph'])
    
    return N, P, K, ph

if __name__ == "__main__":
    city = "Lucknow"  # Change to desired city
    try:
        N, P, K, ph = get_soil_values_by_city(city)
        print(f"Soil values for {city}:")
        print(f"N: {N}")
        print(f"P: {P}")
        print(f"K: {K}")
        print(f"pH: {ph}")
    except ValueError as e:
        print(e)
