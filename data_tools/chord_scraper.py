## Scrape Chords from https://www.e-chords.com/chords/artist/song
## and append to a text file

##NOTE: output file must already exist and must have "chords" \n as header on first line
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import sys

# take the urls entered via the command line and save them as a list
urls = []
for u in sys.argv:
    urls.append(u)
    print(u)

print(urls)
#remove the first url cause it's actually your file location
urls.pop(0)

hdr = {"User-Agent": "Mozilla/5.0"}

for url in urls:
    request_site = Request(url, headers=hdr)
    webpage = urlopen(request_site).read()

    soup = BeautifulSoup(webpage, 'html.parser')
    o = open("output.csv", 'a')
    for text in soup.find_all('u'):
        o.write(text.get_text() + '\n')

    print("Scraped chords from " + url)
