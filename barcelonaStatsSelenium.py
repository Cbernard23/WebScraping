import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get("https://fcbarcelona.com/football/first-team/results?competitionId=0&month=0&temporada=602")
time.sleep(1)

elements = browser.find_element_by_tag_name("body")


numOfPageDowns = 10

while numOfPageDowns:
	elements.send_keys(Keys.PAGE_DOWN)
	time.sleep(0.2)
	numOfPageDowns -= 1

postElements = browser.find_elements_by_class_name("scoreboard__score__result")