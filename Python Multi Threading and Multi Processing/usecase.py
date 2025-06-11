#https://www.langchain.com/
#https://www.langchain.com/about
#https://blog.langchain.dev/


import threading
import requests
from bs4 import BeautifulSoup
import time

urls = ['https://www.langchain.com/',
'https://www.langchain.com/about',
'https://blog.langchain.dev/'
]

def fetch_contents(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(f"Fetched {len(soup.text)} characters from {url}")

threads = []

for url in urls:
    thread = threading.Thread(target=fetch_contents,args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All Webpages Fetched")
