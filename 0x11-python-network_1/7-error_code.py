#!/usr/bin/python3

"""
This script sends a request to a url and displays the response body.
    Usage: ./7-error_code.py <url>
"""
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]

    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    print(response.text)
