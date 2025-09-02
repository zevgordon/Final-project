import requests

payload = {
    "machine": "pc1",
    "data": "Hello world keystrokes from test script"
}

response = requests.post("http://127.0.0.1:5000/api/upload", json=payload)
print(response.json())
