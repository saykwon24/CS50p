import requests

def get_artworks(query, limit):
    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search",
            {"q": query, "limit": limit}    # query parameter로 artwork와 limit를 전달
        )
        response.raise_for_status()
    except requests.HTTPError:
        return []
    
    content = response.json()
    return [artwork["title"] for artwork in content["data"]]


def get_artists(query, limit):
    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/agents/search",
            {"q": query, "limit": limit}    # query parameter로 artist와 limit를 전달
        )
        response.raise_for_status()
    except requests.HTTPError:
        return []
    
    content = response.json()
    return [artist["title"] for artist in content["data"]]