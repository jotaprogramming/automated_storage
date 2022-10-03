import requests

url = "https://api.themoviedb.org/3/movie/popular"

arr = []

for i in range(0, 10):
    querystring = {
        "api_key": "af2c420e596f08347a8c9d2b1d756b7e",
        "language": "en-US",
        "page": str(i + 1),
    }
    response = requests.request("GET", url, params=querystring)
    results = response.json()
    arr.append(results["results"])

data = arr

# print(data)
