import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/75.0.3770.100 Safari/537.36"
}

res = requests.get("http://127.0.0.1:8000/", headers=headers)

print(res.status_code)
print(res.text)
