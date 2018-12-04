import json

import pygal_maps_world.maps
from pygal.style import LightColorizedStyle, RotateStyle

from country_codes import get_country_code

filename = 'gdp_json.json'
year = 2015

with open(filename) as f:
    data = json.load(f)

    cc_gdp = {}
    for gdp_dict in data:
        if year == gdp_dict['Year']:
            cc = get_country_code(gdp_dict['Country Name'])
            if cc:
                cc_gdp[cc] = float(gdp_dict['Value'])

worldmap_chart = pygal_maps_world.maps.World()
worldmap_chart.add('GDP in ' + str(year), cc_gdp)
worldmap_chart.render_to_file('gdp_json.svg')