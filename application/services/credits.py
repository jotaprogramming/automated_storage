import requests

def getCast(id):
    url = f"https://api.themoviedb.org/3/movie/{str(id)}/credits"

    querystring = {"api_key":"af2c420e596f08347a8c9d2b1d756b7e"}

    response = requests.request("GET", url, params=querystring)

    data = response.json()
    
    return data["cast"]

# print(len(getCast(118)))