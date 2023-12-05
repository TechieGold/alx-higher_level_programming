#!/usr/bin/python3
"""
This script sends a POST request to the specified URL
with the given email parameter.

    Usage: ./2-post_email.py <URL> <email>
        - Displays the body of the response.
"""
import sys
from urllib.parse import urlencode
from urllib.request import urlopen, Request

if __name__ == "__main__":
    url = sys.argv[1]
    email = {"email": sys.argv[2]}
    encoded_email = urlencode(email).encode("ascii")

    request = Request(url, encoded_email)
    with urlopen(request) as response:
        print(response.read().decode("utf-8"))
