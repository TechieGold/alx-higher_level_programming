#!/usr/bin/python3
"""
This script fetches the value of X-Request-Id variable
from the header of the response.
"""
from urllib.request import urlopen
import sys
url = sys.argv[1]

if __name__ == "__main__":
    with urlopen(url) as response:
        content = response.getheader('X-Request-Id')
        print(content)
