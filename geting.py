import requests
response = requests.get("https://www.flickr.com/services/rest/?method=flickr.photos.getPopular&api_key=42283f01b9a7bc7378f7688495144d70&user_id=194125240%40N08&format=json&nojsoncallback=1")

print(response.status_code)
print(response.json())