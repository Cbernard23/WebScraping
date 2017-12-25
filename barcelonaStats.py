import requests
from bs4 import BeautifulSoup


# The pages for each season
page2011 = requests.get("https://fcbarcelona.com/football/first-team/results?competitionId=0&month=0&temporada=602", data={'start':0})
page2012 = requests.get("https://fcbarcelona.com/football/first-team/results?competitionId=0&month=0&temporada=603")
page2013 = requests.get("https://fcbarcelona.com/football/first-team/results?competitionId=0&month=0&temporada=604")
page2014 = requests.get("https://fcbarcelona.com/football/first-team/results?competitionId=0&month=0&temporada=605")
page2015 = requests.get("https://fcbarcelona.com/football/first-team/results?competitionId=0&month=0&temporada=606")
page2016 = requests.get("https://fcbarcelona.com/football/first-team/results?competitionId=0&month=0&temporada=607")

soup = BeautifulSoup(page2011.content, 'html.parser')

scores = soup.find_all('span', class_='scoreboard__score__result')

print(scores)




#print(soup.prettify())
#htmlList = [type(item) for item in list(soup.children)]

#print(htmlList)

#html = list(soup.children)[5]
#print(html)
#eles = list(html.children)
#print(eles)