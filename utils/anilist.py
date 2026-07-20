import requests


ANILIST_URL = "https://graphql.anilist.co"



def search_anime(name):

    query = """

    query ($search: String) {

        Media(search: $search, type: ANIME) {

            title {
                romaji
                english
            }

            coverImage {
                large
            }

            genres

            averageScore

            episodes

            status
        }
    }

    """



    variables = {
        "search": name
    }



    try:

        response = requests.post(
            ANILIST_URL,
            json={
                "query": query,
                "variables": variables
            }
        )


        data = response.json()


        media = data["data"]["Media"]


        return {

            "title": media["title"]["english"]
            or media["title"]["romaji"],

            "image": media["coverImage"]["large"],

            "genres": ", ".join(
                media["genres"]
            ),

            "score": media["averageScore"],

            "episodes": media["episodes"],

            "status": media["status"]

        }



    except Exception:

        return None