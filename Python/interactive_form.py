import mechanicalsoup 


url = "http://olympus.realpython.org/login"
browser = mechanicalsoup.Browser()
page = browser.get(url)

login_page = browser.get(url)
login_html = login_page.soup

form = login_html.select("form")[0]
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"


profiles_page = browser.submit(form, login_page.url)
links = profiles_page.soup.select("a")
for link in links:
    address = link['href']
    text = link.text
    print(f"{text}:{address}")
print(profiles_page.url)
