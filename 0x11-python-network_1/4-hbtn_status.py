#!/usr/bin/python3
if __name__ == "__main__":

    import requests as req
    
    http = req.get("https://intranet.hbtn.io/status")
    http = http.text
    print("Body response:")
    print("\t- type: {}".format(type(http)))
    print("\t- content: {}".format(http))
