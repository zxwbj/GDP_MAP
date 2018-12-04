from pygal_maps_world.i18n import COUNTRIES


def get_country_code(country):
    for key in COUNTRIES.keys():
        if country == COUNTRIES[key]:
            return key
    return None
