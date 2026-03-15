from bs4 import BeautifulSoup
import requests

url = "http://www.nytimes.com/"
r = requests.get(url)
htmlContent = r.text

nyTimes = BeautifulSoup(htmlContent, 'html.parser')
print(nyTimes)