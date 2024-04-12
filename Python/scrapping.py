from urllib.request import urlopen
from bs4 import  BeautifulSoup as bs
import re


url = "http://olympus.realpython.org/profiles/aphrodite"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
soup = bs(html, "html.parser")
print(soup.get_text())



print(html)
print(re.findall("a.*c", "abbc"))
print(re.findall("a.*c", "abdc"))

