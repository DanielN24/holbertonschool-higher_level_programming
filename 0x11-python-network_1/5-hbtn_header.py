#!/usr/bin/python3
"""displays the value of the variable X-Request-Id """

if __name__ == "__main__":

    import requests
    import sys

    resp = requests.get(sys.argv[1])
    print(resp.headers("X-Request-Id"))
