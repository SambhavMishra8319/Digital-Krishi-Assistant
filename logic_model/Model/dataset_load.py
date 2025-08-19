import pandas as pd
from sklearn.preprocessing import LabelEncoder
import sys
print(sys.executable)

def load_data(path="Dataset/Crop_recommendation.csv"):
    data = pd.read_csv(path)
    X = data.drop('label', axis=1)
    y = data['label']

    le = LabelEncoder()
    y_encoded = le.fit_transform(y)

    return X, y_encoded, le
