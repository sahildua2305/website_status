# Author{
# 	name: sahildua2305
# 	url : http://sahildua.com
# }

import requests

headers = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36"

# function to check whether a website is down or not
# params{
# 	url: Website url to be checked
# }
# returns{
# 	True : if website is up
# 	False: if website is down
# }
def website_up(url=""):
	if url=="":
		return False
	try:
		response = requests.get(url, headers={'user_agent': headers}, timeout=15)
		if response.status_code==200:
			return True
		return False
	except requests.exceptions.Timeout, requests.exceptions.ConnectionError:
		return False

# function to check whether a website is down or not
# params{
# 	url: Website url to be checked
# }
# returns{
# 	True : if website is down
# 	False: if website is up
# }
def website_down(url=""):
	return not website_up(url)

# function to check whether a website is down or not
# params{
# 	url: Website url to be checked
# }
# returns{
# 	-1: if website is invalid or connection timed out
# 	10x or 20x or 30x or 40x or 50x HTTP standard code if requests returns a valid HTTP code
# }
def website_code(url=""):
	if url=="":
		return -1
	try:
		response = requests.get(url, headers={'user_agent': headers}, timeout=15)
		return response.status_code
	except requests.exceptions.Timeout, requests.exceptions.ConnectionError:
		return -1