#!/usr/bin/python3
"""A python script that fetches https://alx-intranet.hbtn.io/status"""

from urllib.request import urlopen
url = "https://alx-intranet.hbtn.io/status"

if __name__ == "__main__":
    with urlopen(url) as response:
        content = response.read()
        print("Body response:")
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content}")
        print(f"\t- utf8 content: {content.decode('UTF-8')}")
