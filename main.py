# Spotipy documentation taken from: https://spotipy.readthedocs.io/en/2.19.0/#api-reference
from bs4 import BeautifulSoup
import requests
from datetime import datetime

import spotipy
# get user_id etc
from spotipy.oauth2 import SpotifyOAuth

# from spotify development
CLIENT_ID = # put your client_id here
CLIENT_SECRET = # put your client secret here

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth
    (
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri="http://example.com",
        scope="playlist-modify-private",
        show_dialog=True,
        cache_path="token.txt"
    )
)

the_date = input("Which date you want to travel back to?(YYYY-MM-DD): ")
# validate the date format
try: datetime.strptime(the_date, "%Y-%m-%d")
except ValueError as error_message:
    print(f"The key {error_message}.")
else:
    print("Thanks for the input!")
    year = int(the_date[:4])

    month = int(the_date[5:7])
    day = int(the_date[8:11])

response = requests.get("https://www.billboard.com/charts/hot-100")
billboard_url_webpage = response.text

soup = BeautifulSoup(billboard_url_webpage, "html.parser")
song_names_spans = soup.find_all("span", class_="chart-element__information__song")
song_names = [song.getText() for song in song_names_spans]

# ------------------------------------search spotify for the song names-------------------------------------------
user_id = sp.current_user()["id"]
song_uris = []

for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        # get hold of all the song uris
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped!")


# ------------------------------------creating and adding to spotify playlist------------------------------------

playlist = sp.user_playlist_create(user=user_id, name=f"{the_date} Billboard 100", public=False)
print(playlist)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)