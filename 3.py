import requests
url = "http://127.0.0.1:8000?username=hacker&password=hacking"
req = requests.get(url)
if 199 < req.status_code < 300:
    print(req.text)
else:
    print(f"Something went wrong, ERROR CODE: {req.status_code}")