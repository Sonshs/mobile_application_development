import urllib, requests, json
#
userinput = input("Nhap tuples (lat, long): ")  # 10.881784, 106.804496
latlng = userinput.replace(" ", "")
# 10.881784, 106.804496
key = 'AIzaSyAilCHbDxJRP2V2ddqiNzYpEZmTof1R4fg'# api key
lang = 'vi' # chon tieng viet
url = "https://maps.googleapis.com/maps/api/geocode/json?latlng=" + latlng + "&language=" + lang + "&key=" + key

# print(url)
with urllib.request.urlopen(url) as response:   # truy cap dia chi
   html = response.read()
# print(response.status)
data = json.loads(html)                         # doc du lieu theo JSON
print(data["results"][0]["formatted_address"])  #In dia chi