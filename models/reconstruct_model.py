import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import joblib

#  original dataset (with missing values)
df = pd.read_csv("data/lora_data.csv")

# Remove duplicates
df = df.drop_duplicates()

# Separate complete & missing data
complete_data = df.dropna(subset=['latitude', 'longitude'])
missing_data = df[df['latitude'].isnull()]

# Feature selection
features = ['speed', 'direction', 'signal_strength']

X = complete_data[features]
y_lat = complete_data['latitude']
y_lon = complete_data['longitude']

# Train models
model_lat = RandomForestRegressor(n_estimators=100, random_state=42)
model_lon = RandomForestRegressor(n_estimators=100, random_state=42)

model_lat.fit(X, y_lat)
model_lon.fit(X, y_lon)

# Predict missing values
X_missing = missing_data[features]

pred_lat = model_lat.predict(X_missing)
pred_lon = model_lon.predict(X_missing)

# Fill predicted values
df.loc[df['latitude'].isnull(), 'latitude'] = pred_lat
df.loc[df['longitude'].isnull(), 'longitude'] = pred_lon

# Evaluation
X_train, X_test, y_train, y_test = train_test_split(X, y_lat, test_size=0.2)

pred_test = model_lat.predict(X_test)

print("Latitude MAE:", mean_absolute_error(y_test, pred_test))

# Save models
joblib.dump(model_lat, "models/model_lat.pkl")
joblib.dump(model_lon, "models/model_lon.pkl")

df.to_csv("data/reconstructed_lora_data.csv", index=False)

print("\n Reconstruction Complete & Model Saved!")
