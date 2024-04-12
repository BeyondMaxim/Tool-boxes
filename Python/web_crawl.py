import requests
from bs4 import BeautifulSoup

# URL of the website to crawl
url = "https://www.geeksforgeeks.org/python-programming-language/"

# Making a GET request 


# check status code for response received 
# success code - 200 

# Send a GET request to the website
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")
print(soup.prettify())
print(soup.title)
print(soup.title.name)
print(soup.title.parent.name)

# Find and print the titles of all products on the website
s = soup.find("div", class_="entry-content")
content = s.find_all('p')
print(content)

    
    #The successful completion of this project will result in a comprehensive and accurate dataset, delivered in an Excel format, ready for analysis and business application.

#If you have the expertise and are interested in this opportunity, please apply with your portfolio showcasing relevant scraping projects. We look forward to your proposal!

#Sample websites:

#https://inla1.org/?s=&category=&location=&a=true
#https://indylandscape.com/directory
#https://my.asla.org/my-asla/directories/firm_search.aspx