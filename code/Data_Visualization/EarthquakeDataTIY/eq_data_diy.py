from plotly.graph_objs import Scattergeo, Layout
import json
from plotly import offline

file = './eq_data_30_day_m1_r.json'

with open(file, encoding='utf-8') as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

mags, longs, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(float(eq_dict['properties']['mag']))
    longs.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_texts.append(f"{eq_dict['properties']['place']}]\n{eq_dict['properties']['title']}")

# Visualize the data on the plotly map
data = [{
    'type' : 'scattergeo',
    'lon' : longs,
    'lat' : lats,
    'text' : hover_texts,
    # Change hovering appearences
    'marker' : {
        'size' : [mag*5 for mag in mags],
        'color' : mags,
        'colorscale' : 'Viridis',
        'reversescale' : True,
        'colorbar' : {'title' : 'magnitude'}
    }
    }
]

title = all_eq_data['metadata']['title']
my_layout = Layout(title=title)

offline.plot({'data' : data, 'layout': my_layout}, filename='./eqdata.html')