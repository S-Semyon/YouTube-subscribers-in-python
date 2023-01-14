#author: https://github.com/S-Semyon
import re
import urllib.request
url = input("Insert a link to the channel: ")

def subs(channel_url: str):
    with urllib.request.urlopen(channel_url) as response:
        html = response.read().decode("utf-8")
    result = re.findall(r'subscriberCountText.*simpleText', str(html))
    result = re.findall(r'label.*s', str(result))
    result = result[0][8:][:-6]
    return result

print(subs(url))