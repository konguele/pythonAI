import requests
from bs4 import BeautifulSoup

def search_internet(query):
    response = requests.get(f"https://www.google.com/search?q={query}")
    soup = BeautifulSoup(response.text, 'html.parser')
    results = []
    for g in soup.find_all(class_='BVG0Nb'):
        results.append(g.text)
    return results[:5]

