import socket
import requests

with open('urls.txt', 'r') as url:
    url_list = url.readlines()
    new_list = [x.replace('\n', '') for x in url_list]

def check_headers(response, header):
    value = response.headers.get(header)
    if value is not None:
        print(f"    [Pass]   '{header}'    {value}")
        return True
    print(f"    [FAIL]       NO '{header}' Header Present")
    return False

def header_resolver():
    for url in new_list:
        res = requests.get(url)
        print("URL Inspected: " + str(url))
        host = url.split("/")[2]
        print("IP Address: " + socket.gethostbyname(host))
        if "https://" in url:
            check_headers(res, "Strict-Transport-Security")
        else:
         print("    [FAIL]       Connected over HTTP,ignoring 'Strict-Transport-Security' check")
        check_headers(res, "Content-Security-Policy")
        check_headers(res, "X-Frame-Options")
        check_headers(res, "Server")
        print("\n")

header_resolver()
