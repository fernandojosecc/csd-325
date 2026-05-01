"""
city_functions.py
Author: Fernando Contreras
Assignment: CSD-325 Module 7
Description: Function that accepts a city and country name and returns
             a formatted string in the form City, Country.
"""


def city_country(city, country, population=None, language=None):
    """Return a formatted string with city, country, optional population and language.

    Parameters:
        city (str): Name of the city.
        country (str): Name of the country.
        population (int, optional): Population of the city.
        language (str, optional): Primary language spoken.

    Returns:
        str: Formatted string, e.g. 'Santiago, Chile - population 5000000, Spanish'
    """
    result = f"{city.title()}, {country.title()}"
    if population:
        result += f" - population {population}"
    if language:
        result += f", {language.title()}"
    return result


if __name__ == "__main__":
    # Call the function three times
    print(city_country("santiago", "chile", 5000000, "spanish"))
    print(city_country("tokyo", "japan", 13960000, "japanese"))
    print(city_country("paris", "france", 2161000, "french"))