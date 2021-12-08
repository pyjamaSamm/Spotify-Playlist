# Spotify-Playlist
Travel back in time to listen to the top 100 Billboard Songs in Spotify Playlist of that particular date!

Project Name : Spotify Playlist

Author : Gulafsha Ahmed

Language : Python

This project helps users to travel back in time and to listen to top 100 Billboard Songs of that date! User needs to enter the date they want to travel back to and by a Spotify Playlist will be automatically generated! This project uses Beautiful Soup, a Python package for parsing HTML and XML documents to scrape data from https://www.billboard.com/charts/hot-100/. It uses Spotipy to get user_id. Spotify for developers gives access to CLIENT_ID and CLIENT_SECRET which needs to be entered in main.py. This project also makes use of requests and datetime modules of python.

main.py : performs the functionality of the project. User needs to put their own CLIENT_ID and CLIENT_SECRET from Spotify for developers after signing up at https://developer.spotify.com. They also need to put their access token in token.txt. Spotipy documentation: https://spotipy.readthedocs.io/en/2.19.0/#api-reference.

token.txt : contains the access token.
