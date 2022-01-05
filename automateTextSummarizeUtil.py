from bs4 import BeautifulSoup
from requests import get
from requests.api import request

url = "https://medium.com/@rahulbhatt1899"


def getText(url):
    page = get(url)
    soup = BeautifulSoup(page.content, "lxml")
    text = ' '.join(map(lambda p: p.text, soup.find_all('div')))
    title = ' '.join(soup.title.stripped_strings)
    return title  , text

text = getText(url)

from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords

print(f"Title : {text[0]}")
print(f"Summary : {summarize(repr(text[1]), word_count = 111)}")