import json
import requests

headers = {
'Content-Type': 'text/plain',
'Referer': 'https://www.icloud.com/sharedalbum/zh-cn/?from=groupmessage&isappinstalled=0',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
}


with open("webstream.txt") as f:
    data = f.read()
    
data = json.loads(data)

photoGuids = []

for i in data["photos"]:
    photoGuids.append(i["photoGuid"])





def download(uid):
    url = "https://p24-sharedstreams.icloud.com/B0OG6XBubZrOLh/sharedstreams/webasseturls"
    d = {"photoGuids": [uid]}
    r = requests.post(url,headers=headers,data=json.dumps(d))
    data = r.json()
    m = 1
    for i in data["items"]:
        url = "https://" + data["items"][i]["url_location"] + data["items"][i]["url_path"]
        #print(url)
        r = requests.get(url,headers=headers)
        with open(uid + str(m) + ".jpg","wb") as f:
            f.write(r.content)
        m += 1

n = 0

for uid in photoGuids:
    try:
        download(uid)
    except:
        pass
    n += 1
    print("已经完成：" + str(n) + "/"  + str(len(photoGuids)))
