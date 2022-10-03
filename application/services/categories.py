import requests

url = "https://api.themoviedb.org/3/genre/movie/list"

querystring = {"api_key":"af2c420e596f08347a8c9d2b1d756b7e","language":"en-US"}

response = requests.request("GET", url, params=querystring)

results = response.json()

data = results["genres"]