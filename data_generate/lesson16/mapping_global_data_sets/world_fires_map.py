import csv
import math

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


filename = 'data/world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.DictReader(f)

    frps, lons, lats = [], [], []

    for row in reader:
        lon = float(row['longitude'])
        lat = float(row['latitude'])
        try:
            frp = float(row['frp'])
        except ValueError:
            print(f"Missing data for {lon}{lat}")
        else:
            frps.append(frp)
            lons.append(lon)
            lats.append(lat)

data = [{
    'type': 'scattergeo',
    'lon' : lons,
    'lat' : lats,
    'marker': {
        'size': [math.log(f + 1) * 5 for f in frps],
        'color': frps,
        'colorscale': 'YlOrRd',
        'colorbar': {'title': 'Fire Radiative Power'},
    },
}]
my_layout = Layout(title = "World - Fires")

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_fires.html')
