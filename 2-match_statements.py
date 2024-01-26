#!/usr/bin/python3

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