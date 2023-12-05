# 0x10. Python - Network #0


In this networking project, I used `curl` in Bash scripts to send different types of messages to websites. It helped me understand how web addresses (URLs) work, the names of websites, and the various messages websites use to communicate (HTTP headers and status codes). I also learned how to use cookies.

As a separate task, I took on a coding challenge [ 6-peak.py](https://github.com/TechieGold/alx-higher_level_programming/blob/master/0x10-python-network_0/6-peak.py) It was about solving problems using Python.

# Tasks 📃

**NOTE:** 
The Bash scripts' curl behavior was designed to interact with a server hosted on a container supplied by ALX.

## 0. cURL body size
- [0-body_size.sh](https://github.com/TechieGold/alx-higher_level_programming/blob/master/0x10-python-network_0/0-body_size.sh): Bash script that sends a GET request to a given URL and displays the size of the response body in bytes.

## 1. cURL to the end
- [1-body.sh](https://github.com/TechieGold/alx-higher_level_programming/blob/master/0x10-python-network_0/1-body.sh): Bash script that sends a GET request to a given URL and displays the response body for a 200 status code response.


## 2. cURL Method
- [2-delete.sh](https://github.com/TechieGold/alx-higher_level_programming/blob/master/0x10-python-network_0/2-delete.sh): Bash script that sends a DELETE request to a given URL and displays the response body.

## 3. cURL only methods
- [3-methods.sh](https://github.com/TechieGold/alx-higher_level_programming/blob/master/0x10-python-network_0/3-methods.sh): Bash script that displays all HTTP methods the server of a given URL will accept.

## 4. cURL headers
- [4-header.sh](https://github.com/TechieGold/alx-higher_level_programming/blob/master/0x10-python-network_0/4-header.sh): Bash script that sends a GET request to a given URL with a header variable X-School-User-Id=98 and displays the response body.

## 5. cURL POST parameters
- [5-post_params.sh](https://github.com/TechieGold/alx-higher_level_programming/blob/master/0x10-python-network_0/5-post_params.sh): Bash script that sends a POST request to a given URL with the variables email=test@gmail.com and subject=I will always be here for PLD and displays the response body.

## 6. Find a peak
- [6-peak.py](https://github.com/TechieGold/alx-higher_level_programming/blob/master/0x10-python-network_0/6-peak.py): [Technical interview preparation] - Python program that finds a peak in a list of unsorted integers.
- [6-peak.txt](https://github.com/TechieGold/alx-higher_level_programming/blob/master/0x10-python-network_0/6-peak.txt): Text file containing the complexity of the algorithm.

## 7. Only status code
- [100-status_code.sh](https://github.com/TechieGold/alx-higher_level_programming/blob/master/0x10-python-network_0/100-status_code.sh): Bash script that sends a GET request to a given URL without using pipes, redirections, ;, or && and displays the status code of the response.

## 8. cURL a JSON file
- [101-post_json.sh](https://github.com/TechieGold/alx-higher_level_programming/blob/master/0x10-python-network_0/101-post_json.sh): Bash script that sends a JSON POST request with the contents of a provided file to a given URL, and displays the response body.

## 9. Catch me if you can!
- [102-catch_me.sh](https://github.com/TechieGold/alx-higher_level_programming/blob/master/0x10-python-network_0/102-catch_me.sh): Bash script that sends a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing "You got me!" in the response body.
