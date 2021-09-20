"""
FAILURE
"""
import csv
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

file = 'world_fires_7_day.csv'
with open(file) as f:
    fire_data = csv.reader(f)
    header_row = next(fire_data)
    print(header_row.index('frp'))
    next_row = next(fire_data)

    lons, lats, frps, dates = [], [], [], []
    for row in fire_data:
        lons.append(row[header_row.index('longitude')])
        lats.append(row[header_row.index('latitude')])
        frps.append(float(row[header_row.index('frp')]))
        dates.append(row[3])

    data = [
        {
            'type' : 'scattergeo',
            'lon' : lons,
            'lat' : lats,
            'text' : dates,
            'marker' : {
                'size' : [frp*5 for frp in frps],
                'color' : frps,
                'colorscale' : 'Viridis',
                'colorbar' : {'title': 'Magnitude'}
            }
        }
    ]

    title = "Fires around the world during past seven days"
    my_layout = Layout(title=title)

    offline.plot({'data':data, 'layout':my_layout}, filename='./firedata.html')
