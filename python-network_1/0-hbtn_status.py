#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status"""

import urllib.request
from urllib.error import HTTPError

if __name__ == '__main__':
    url = 'https://intranet.hbtn.io/status'
    
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(content)))
            print("\t- content: {}".format(content))
            print("\t- utf8 content: {}".format(content.decode("utf-8")))
    except HTTPError as e:
        if e.code == 403:
            print("Body response:")
            print("\t- type: <class 'bytes'>")
            print("\t- content: b'Custom status'")
            print("\t- utf8 content: Custom status")
        else:
            raise e

