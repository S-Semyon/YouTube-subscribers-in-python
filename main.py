#author: https://github.com/S-Semyon
import re
import urllib.request
url = input("Insert a link to the channel: ")

def subs(channel_url: str):
    with urllib.request.urlopen(channel_url) as response:
        html = response.read().decode("utf-8")
    result = re.findall(r'subscriberCountText.{0,150}simpleText', str(html))
    result = re.search(r'label.*s', str(result[-1]))
    result = result[0][8:][:-6]
    return result

print(subs(url))
