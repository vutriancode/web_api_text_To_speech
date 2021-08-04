import json
import requests
headers = {"Authorization": "Bearer MY ACCESS TOKEN"} 
para = {
    "name": "TEST.jpg", 
    "parents": ["MY FOLDER ID"] 
}
files = {
    'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
    'file': ('image/jpeg', open("./TEST.jpg", "rb"))
}
r = requests.post(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=headers,
    files=files
)
print(r.text)