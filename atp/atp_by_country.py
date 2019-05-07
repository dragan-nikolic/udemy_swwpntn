from selenium import webdriver

BASE_URL = "https://www.atptour.com/en/rankings/singles"

DRIVER_LOCATION = "/Users/dragan/tools/webdriver/chromedriver"

class AtpByCountry():

    def ranking_by_country(self):
        driver = webdriver.Chrome(DRIVER_LOCATION)
        driver.get(BASE_URL)
        # elementById = driver.find_element_by_id("name")

        # if elementById is not None:
        #     print("We found an element by Id")

        # elementByName = driver.find_element_by_name("show-hide")

        # if elementByName is not None:
        #     print("We found an element by Name")


atp = AtpByCountry()
atp.ranking_by_country()
