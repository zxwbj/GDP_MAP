import csv

import pygal_maps_world.maps
from pygal.style import LightColorizedStyle, RotateStyle

from country_codes import get_country_code


filename = 'gdp_csv.csv'
year = '2016'

with open(filename) as f:
    data = csv.reader(f)

    cc_gdp = {}
    for row in data:
        if year == row[2]:
            cc = get_country_code(row[0])
            if cc:
                cc_gdp[cc] = float(row[3])

worldmap_chart = pygal_maps_world.maps.World()
worldmap_chart.add('GDP in 2016', cc_gdp)
worldmap_chart.render_to_file('gdp_csv.svg')

