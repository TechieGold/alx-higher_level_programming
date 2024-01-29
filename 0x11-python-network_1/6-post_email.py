#!/usr/bin/python3

"""
A script that sends a POST request to a given URL with a given email
Usage: ./6-post_email.py <url> <email>
"""
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    response = requests.post(url, data=value)
    print(response.text)
