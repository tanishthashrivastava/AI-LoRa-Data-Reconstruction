import pandas as pd

df = pd.read_csv("data/lora_data.csv")

print("🔹 Initial Shape:", df.shape)

# 1. Duplicate Removal
df = df.drop_duplicates()
print("After removing duplicates:", df.shape)

# 2. Missing Values Check
print("\nMissing Values:\n", df.isnull().sum())

# 3. Missing Value Handling 
# Sort data by device and time
df = df.sort_values(by=["device_id", "timestamp"])

# Forward fill (previous value)
df[['latitude','longitude']] = df.groupby('device_id')[['latitude','longitude']].ffill()

# Backward fill (next value)
df[['latitude','longitude']] = df.groupby('device_id')[['latitude','longitude']].bfill()

# 4. Final Check
print("\nAfter Filling Missing Values:\n", df.isnull().sum())

print("\nSample Data:\n", df.head())

# Save cleaned dataset
df.to_csv("data/cleaned_lora_data.csv", index=False)

print("\n Cleaned dataset saved!")
