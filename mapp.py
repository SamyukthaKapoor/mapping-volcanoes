import folium
import pandas as pd
data = pd.read_csv("Volcanoes.csv")
lon=list(data["LON"])
lat=list(data["LAT"])
map=folium.Map(location=[38.91,-99.07],zoom_start=6)
for lt , ln in zip(lat, lon):
    map.add_child(folium.Marker(location=[lt,ln], popup="volcano", icon=folium.Icon(color='green')))
map.save("pandas.html")
