'''from zillow_api import ZillowAPI

zillow_api_client = ZillowAPI("INSERT_YOUR_API_KEY")

search_result = zillow_api_client.search(
	params={
		"keyword": "new york, ny",
		"type": "forSale",
		"price[min]": 1000000,
		"price[max]": 2000000,
		"homeTypes": ["house", "apartment"]
	}
)

print(search_result)'''

import requests
import xml.etree.ElementTree as ET

def zillow_property_search(address, city, state, zip_code, zws_id):
    url = f"http://www.zillow.com/webservice/GetDeepSearchResults.htm?zws-id={zws_id}&address={address}&citystatezip={city}%2C+{state}+{zip_code}"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            root = ET.fromstring(response.content)
            result = root.find('response/results/result')
            llc = result.find("zestimate/valuationRange/low").text
            owner = result.find("owner/ownerDisplayName").text
            return llc, owner
        else:
            print(f"Request failed with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the request: {e}")
    
    return None, None

# Replace the following variables with your own values
address = "123 Main St"
city = "Los Angeles"
state = "CA"
zip_code = "90001"
zws_id = "9b9a6d5e-3ce9-423a-ad59-e7904bd39b7b"

llc, owner = zillow_property_search(address, city, state, zip_code, zws_id)
if llc and owner:
    print(f"LLC: {llc}")
    print(f"Owner: {owner}")
else:
    print("Failed to retrieve property information.")
    