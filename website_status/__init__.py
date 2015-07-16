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
	if url=="":
		return True
	try:
		response = requests.get(url, headers={'user_agent': headers}, timeout=15)
		if response.status_code==200:
			return False
		return True
	except requests.exceptions.Timeout, requests.exceptions.ConnectionError:
		return True