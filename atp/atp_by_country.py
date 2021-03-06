"""
{country: points, ...}
{country: {player: points, ...}, ...}
"""

from selenium import webdriver

BASE_URL = "https://www.atptour.com/en/rankings/singles"

DRIVER_LOCATION = "/Users/dragan/tools/webdriver/chromedriver"

class AtpByCountry():

    def ranking_by_country(self):
        driver = webdriver.Chrome(DRIVER_LOCATION)
        driver.get(BASE_URL)

        countries = {}
        countries_players = {}

        table = driver.find_element_by_class_name("mega-table")
        tbody = table.find_element_by_tag_name("tbody")
        rows = tbody.find_elements_by_tag_name("tr")
        for row in rows:
            cells = row.find_elements_by_tag_name("td")
            player = cells[3].text
            country = cells[2].find_element_by_tag_name("img").get_attribute("alt")
            points = int(cells[5].text.replace(',', ''))

            if country in countries:
                countries[country] += points
            else:
                countries[country] = points
                countries_players[country] = {}

            countries_players[country][player] = points

        sorted_countries = sorted(
                                countries.items(), 
                                key=lambda kv: kv[1], 
                                reverse=True)

        ix = 1
        for country in sorted_countries:
            print("{}. {}: {}".format(ix, country[0], country[1]))
            country_players =  countries_players[country[0]]
            for player in country_players:
                print("--- {}: {}".format(player, country_players[player]))

            ix += 1

atp = AtpByCountry()
atp.ranking_by_country()
