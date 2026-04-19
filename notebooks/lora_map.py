import pandas as pd
import folium
import webbrowser
import os

# Load reconstructed data
df = pd.read_csv("data/reconstructed_lora_data.csv")

# Map center
center_lat = df['latitude'].dropna().mean()
center_lon = df['longitude'].dropna().mean()

# Create map
m = folium.Map(
    location=[center_lat, center_lon],
    zoom_start=13
)

# Add markers 
for _, row in df.iterrows():
    if pd.notnull(row['latitude']) and pd.notnull(row['longitude']):
        
        color = 'red' if row['is_fragmented'] == 1 else 'green'

        folium.CircleMarker(
            location=[row['latitude'], row['longitude']],
            radius=6,
            color=color,
            fill=True,
            fill_color=color,
            fill_opacity=0.9,
            popup=f"Device: {row['device_id']} | Fragmented: {row['is_fragmented']}"
        ).add_to(m)

# Add movement path 
coords = df[['latitude','longitude']].dropna().values.tolist()

folium.PolyLine(
    coords,
    color='blue',
    weight=2.5,
    opacity=0.8
).add_to(m)

legend_html = '''
<div style="
position: fixed; 
bottom: 50px; left: 50px; 
width: 180px; height: 100px; 
background-color: white; 
border:2px solid grey; 
z-index:9999; 
font-size:14px;
padding: 10px;
">
<b>Legend</b><br>
<span style="color:green;">●</span> Normal Data<br>
<span style="color:red;">●</span> Reconstructed Data<br>
<span style="color:blue;">―</span> Movement Path
</div>
'''

m.get_root().html.add_child(folium.Element(legend_html))

# Save map
map_path = "data/lora_map.html"
m.save(map_path)

print("Map generated successfully!")

webbrowser.open('file://' + os.path.realpath(map_path)) 
