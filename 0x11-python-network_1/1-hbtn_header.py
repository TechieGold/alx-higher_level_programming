#!/usr/bin/python3
"""
This script fetches the value of X-Request-Id variable
from the header of the response.
"""
import sys
from urllib.request import Request
from urllib.request import urlopen

url = sys.argv[1]

if __name__ == "__main__":
    request = Request(url)
    with urlopen(request) as response:
        x_request_id = dict(response.headers).get("X-Request-Id")
        print(x_request_id)
