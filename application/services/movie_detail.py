import requests

def getMovieDetail(id):

    url = f"https://api.themoviedb.org/3/movie/{str(id)}"

    querystring = {"api_key":"af2c420e596f08347a8c9d2b1d756b7e","append_to_response":"releases"}

    response = requests.request("GET", url, params=querystring)

    return response.json()
    # print(res)
    # data = res["results"]

# getMovieDetail(760161)