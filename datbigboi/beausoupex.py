from bs4 import BeautifulSoup
import requests

popUrl = "http://www.worldometers.info/world-population/population-by-country/"
reqPop = requests.get(popUrl)
#once instance request of popUrl
popData = reqPop.text
#changing the reqpop into text of it, but still html
popSoup = BeautifulSoup(popData, "html.parser")
#runs it though BS and fixes the html shit
#Build for loop to loop through all td elements
#inside for loop: ask for each td element's a-tag text
for thing in popSoup.find_all("a"):
    print(thing.get_text())
