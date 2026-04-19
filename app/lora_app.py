import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from sklearn.ensemble import RandomForestRegressor

st.set_page_config(page_title="LoRa Reconstruction", layout="wide")

st.title("LoRa Data Reconstruction System")

uploaded_file = st.file_uploader("Upload LoRa CSV file", type=["csv"])

if uploaded_file is not None:
    
    df = pd.read_csv(uploaded_file)
    st.subheader("Raw Data")
    st.write(df.head())

    # Remove duplicates
    df = df.drop_duplicates()

    # Separate complete & missing
    complete = df.dropna(subset=['latitude', 'longitude'])
    missing = df[df['latitude'].isnull()]

    if len(missing) > 0:
        st.warning(f"{len(missing)} fragmented records detected")

        features = ['speed', 'direction', 'signal_strength']

        X = complete[features]
        y_lat = complete['latitude']
        y_lon = complete['longitude']

        model_lat = RandomForestRegressor()
        model_lon = RandomForestRegressor()

        model_lat.fit(X, y_lat)
        model_lon.fit(X, y_lon)

        X_missing = missing[features]

        pred_lat = model_lat.predict(X_missing)
        pred_lon = model_lon.predict(X_missing)

        df.loc[df['latitude'].isnull(), 'latitude'] = pred_lat
        df.loc[df['longitude'].isnull(), 'longitude'] = pred_lon

        st.success("Missing values reconstructed using ML")

    else:
        st.info("No missing values found")

    # Map Visualization
    st.subheader("Device Movement Map")

    center_lat = df['latitude'].mean()
    center_lon = df['longitude'].mean()

    m = folium.Map(location=[center_lat, center_lon], zoom_start=13)

    for _, row in df.iterrows():
        color = 'red' if row['is_fragmented'] == 1 else 'green'

        folium.CircleMarker(
            location=[row['latitude'], row['longitude']],
            radius=5,
            color=color,
            fill=True,
            fill_color=color,
            fill_opacity=0.8,
        ).add_to(m)

    # Path
    coords = df[['latitude','longitude']].values.tolist()
    folium.PolyLine(coords, color='blue').add_to(m)

    st_folium(m, width=1000, height=500)

    # Download option
    st.download_button(
        " Download Reconstructed Data",
        df.to_csv(index=False),
        file_name="reconstructed_data.csv"
    )
    