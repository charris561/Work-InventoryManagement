# import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup

# specify the url
url = "https://facserv.uccs.edu/webtma/MainApp.aspx?windowID=2779d3733a5f47bfb20297d41f383a12"

# Connect to the website and return the html to the variable ‘page’
try:
    page = urlopen(url)
except:
    print("Error opening the URL")

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')
