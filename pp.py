
""" flask_example.py
    Required packages:
    - flask
    - folium
    Usage:
    Start the flask server by running:
        $ python flask_example.py
    And then head to http://127.0.0.1:5000/ in your browser to see the map displayed
"""

from flask import Flask

import folium

app = Flask(__name__)

@app.route('/')
def index():
    #Define coordinates of where we want to center our map

    start_coords = [36.664207,-4.458674]
    mis_coords=start_coords
    #Adding a tileset to our map
    map_with_tiles = folium.Map(location = mis_coords, tiles = 'Stamen Toner',zoom_start = 6)
    #Add markers to the map
    folium.Marker(mis_coords,    
        popup="jajja",
        icon=folium.Icon(icon='fa solar-panel', color="blue"),
        draggable=True
        ).add_to(map_with_tiles)



    folium_map = folium.Map(location=start_coords, zoom_start=14)
    return map_with_tiles._repr_html_()


if __name__ == '__main__':
    app.run('0.0.0.0', 8000,debug=True)
