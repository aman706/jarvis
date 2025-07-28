import requests
from bs4 import BeautifulSoup

def google_search(query):
    url = f"https://www.google.com/search?q={query}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    try:
        answer = soup.select_one(".BNeawe span").text
    except:
        answer = "Sorry, I couldn’t find anything specific."
    return answer
