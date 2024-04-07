'''
Crawler class to automate the search across selected online platforms and extract relevant data.
'''
import requests
from bs4 import BeautifulSoup
class Crawler:
    def __init__(self):
        self.base_url = "https://www.cat.com/id_ID.html"
        self.data = []
    def crawl(self, platform, database):
        url = self.base_url + platform
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        # Extract relevant data from the webpage
        for element in soup.find_all("div", class_="lead"):
            lead_data = {
                "name": element.find("span", class_="name").text,
                "contact": element.find("span", class_="contact").text,
                "location": element.find("span", class_="location").text
            }
            database.data.append(lead_data)