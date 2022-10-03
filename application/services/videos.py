import requests


def getVideo(id):
    url = f"https://api.themoviedb.org/3/movie/{str(id)}/videos"

    querystring = {"api_key": "af2c420e596f08347a8c9d2b1d756b7e"}

    response = requests.request("GET", url, params=querystring)

    res = response.json()

    results = res["results"]

    data = 0

    if results and len(results) > 0:
        for item in results:
            if (
                str(item["name"]).lower() == "official trailer"
                and str(item["site"]).lower() == "youtube"
            ):
                data = item
                break
            data = results[0]
    return data

