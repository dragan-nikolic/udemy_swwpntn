from selenium import webdriver

BASE_URL = "https://www.atptour.com/en/rankings/singles"

DRIVER_LOCATION = "/Users/dragan/tools/webdriver/chromedriver"

class AtpByCountry():

    def ranking_by_country(self):
        driver = webdriver.Chrome(DRIVER_LOCATION)
        driver.get(BASE_URL)

        points_per_country = {}

        table = driver.find_element_by_class_name("mega-table")
        tbody = table.find_element_by_tag_name("tbody")
        rows = tbody.find_elements_by_tag_name("tr")
        for row in rows:
            cells = row.find_elements_by_tag_name("td")
            player = cells[3].text
            country = cells[2].find_element_by_tag_name("img").get_attribute("alt")
            points = int(cells[5].text.replace(',', ''))

            if country in points_per_country:
                points_per_country[country] += points
            else:
                points_per_country[country] = points

        sorted_countries = sorted(points_per_country.items(), key=lambda kv: kv[1], reverse=True)

        for country in sorted_countries:
            print("{}: {}".format(country[0], country[1]))


atp = AtpByCountry()
atp.ranking_by_country()
