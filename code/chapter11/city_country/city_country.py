def city_country(city, country, population=""):
    if population:
        formatted_value = f"{city.title()}, {country.title()} - population {population}"
    else:
        formatted_value = f"{city.title()}, {country.title()}"
    return formatted_value