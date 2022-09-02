#!/usr/bin/python3
if __name__ == "__main__":
    
    from urllib.parse import urlencode
    import urllib.request
    import sys
    
    email = {"email": sys.argv[2]}
    emailencode = urlencode(email)
    emailencode = emailencode.encode("ascii")
    req_response = urllib.request.Request(sys.argv[1], emailencode)
    with urllib.request.urlopen(req_response) as response:
        html = response.read()
        print(html.decode("utf-8"))
