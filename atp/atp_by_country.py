from selenium import webdriver

BASE_URL = "https://www.atptour.com/en/rankings/singles"

DRIVER_LOCATION = "/Users/dragan/tools/webdriver/chromedriver"

class AtpByCountry():

    def ranking_by_country(self):
        driver = webdriver.Chrome(DRIVER_LOCATION)
        driver.get(BASE_URL)

        table = driver.find_element_by_class_name("mega-table")
        tbody = table.find_element_by_tag_name("tbody")
        rows = tbody.find_elements_by_tag_name("tr")
        for row in rows:
            cells = row.find_elements_by_tag_name("td")
            print(cells[3].text)
            country = cells[2].find_element_by_tag("img")
            print(country.attr)
        # elementById = driver.find_element_by_id("name")

        # if elementById is not None:
        #     print("We found an element by Id")

        # elementByName = driver.find_element_by_name("show-hide")

        # if elementByName is not None:
        #     print("We found an element by Name")


atp = AtpByCountry()
atp.ranking_by_country()
