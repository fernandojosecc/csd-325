"""
test_cities.py
Author: Fernando Contreras
Assignment: CSD-325 Module 7
Description: Unit tests for the city_country function in city_functions.py.
"""

import unittest
from city_functions import city_country


class TestCityCountry(unittest.TestCase):
    """Tests for the city_country function."""

    def test_city_country(self):
        """Test city and country only."""
        result = city_country("santiago", "chile")
        self.assertEqual(result, "Santiago, Chile")


if __name__ == "__main__":
    unittest.main()