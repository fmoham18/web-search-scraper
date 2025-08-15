# Google custom search engine ID 53c07d74766c84a4a
# programmable search engine api key AIzaSyB7TiC5-22iok7mfKrOCmIzC1xQpf23-YE
# OAuth credentials (?) 105666327542-dvb139roq0pcqvkape9ddkermlukq6nn.apps.googleusercontent.com
from googleapiclient.discovery import build
from bs4 import BeautifulSoup
import requests
import pprint

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

def scrape_url_body(url):
    response = requests.get(url) 
    if response.status_code == 200:
        html_content = response.content
        print(html_content)
        # Use BeautifulSoup to parse the html
        soup = BeautifulSoup(html_content, "html.parser")
        print("Head:")
        print(soup.head)
    else:
        print(response)


search = input("Enter the search query: ")

my_api_key = "AIzaSyB7TiC5-22iok7mfKrOCmIzC1xQpf23-YE"
my_cse_id = "53c07d74766c84a4a"


results = google_search(search, my_api_key, my_cse_id, num=10)

# Have beautiful soup read the body of every site

for result in results:
    scrape_url_body(result['link'])
    # pprint.pprint(result)


# scrape_url_body(input("Enter a url to have scraped: "))