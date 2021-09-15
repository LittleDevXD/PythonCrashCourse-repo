import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Opening file and storing the whole file in a var
file = 'eq_data_30_day_m1.json'
with open(file) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

# Extracting all required data from file
mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_texts.append(f"{eq_dict['properties']['title']}\n{eq_dict['properties']['status']}")

# Visualize data on the map with Plotly
data = [{
    'type' : 'scattergeo',
    'lon' : lons,
    'lat' : lats,
    'text' : hover_texts,
    # Customizing Marker appearance
    'marker' : {
        'size' : [mag*5 for mag in mags],
        'color' : mags,
        'colorscale' : 'Viridis',
        'reversescale' : True,
        'colorbar' : {'title' : 'Magnitude'}
    }
}]

# Rendering the map
title = all_eq_data['metadata']['title']
my_layout = Layout(title=title)

offline.plot({'data':data, 'layout':my_layout}, filename='global_eq.html')

