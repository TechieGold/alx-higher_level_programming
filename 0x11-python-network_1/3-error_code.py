#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to a given URL
and displays the response body.

Usage: ./3-error_code.py <URL>
    - Handles HTTP errors.
"""
from sys import argv
from urllib.error import HTTPError
from urllib.request import urlopen, Request


if __name__ == "__main__":
    url = argv[1]

    request = Request(url)
    try:
        with urlopen(request) as response:
            print(response.read().decode("ascii"))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
