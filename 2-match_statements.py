#!/usr/bin/python3

# This won't work on the terminal because match statements
# were introduced in python version 3.10 and higher but the 
# version on the sandbox is python 3.8.10

def http_error(status):
    match status:
        case 400:
            print('Bad Request')
        case 404:
            print('Not found')
        case 408:
            print('Request timed out')
        case _:
            print("Something's wrong with the Internet")

http_error(404)
