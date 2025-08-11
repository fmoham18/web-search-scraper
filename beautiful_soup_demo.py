from bs4 import BeautifulSoup
import requests

def scrape_url_body(url):
    response = requests.get(url) 
    if response.status_code == 200:
        html_content = response.content
        print(html_content)
        # Use BeautifulSoup to parse the html
        soup = BeautifulSoup(html_content, "html.parser")
        print("Body:")
        print(soup.body)
    else:
        print(response)


scrape_url_body(input("Enter a url to have scraped: "))

