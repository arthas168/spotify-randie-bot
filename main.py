import os
import time
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = os.getenv("SPOTIFY_RANDIE_BOT_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_RANDIE_BOT_CLIENT_SECRET")

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# TODO: should be bool
# TODO: should be in utils file
# toggle theatrical mode
IN_THEATRICAL_MODE = 1


# TODO: should be in utils file
def toggle_sleep(in_theatrical_mode):
    if in_theatrical_mode == 1:
        time.sleep(1)


def welcome_dialogue():
    print("Starting up services...")
    toggle_sleep(IN_THEATRICAL_MODE)
    print("Authenticating with Spotify...")
    toggle_sleep(IN_THEATRICAL_MODE)
    print("Waking Randie up...")
    toggle_sleep(IN_THEATRICAL_MODE)
    print("Greetings human! How may I be of service today?")


welcome_dialogue()

# TODO: input shouldn't need quotes for py to know it's a string (do a cast?)
artist_id = input("Artist ID: ")

# Sammich user ID sm03r80ya0iwzpezo7vve82xq
# AA artist ID 1caBfBEapzw8z2Qz9q0OaQ

artist_name = spotify.artist(artist_id)["name"]
artist_top_tracks = spotify.artist_top_tracks(artist_id)
top_track = artist_top_tracks["tracks"][0]["name"]

print("Top track by " + artist_name + " is " + top_track)
