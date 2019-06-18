def city_country_name(city,country,population=0):
    if population:
        name = city + ' ' + country + ' -population ' + str(population)
    else:
        name = city + ' ' + country
    return name.title()