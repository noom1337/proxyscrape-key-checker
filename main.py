import requests, re

def parse(response):
    status_re = "<h3 class=\"mb-0\">(.*?)</h3>"
    return re.findall(status_re, response)
    
print("# ProxyScrape key checker")
keysFile = open("keys.txt", "r")
for _key in keysFile:
    key = _key.strip()
    data = {
        "key": key
    }
    response = requests.post("https://api.proxyscrape.com/v2/account/unaccess", data=data).text
    parsed_info = parse(response)
    if len(parsed_info) == 3:
        print("$ ~ " + parsed_info[0] + " Proxies: " + parsed_info[1]) 