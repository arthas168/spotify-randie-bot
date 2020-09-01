import os
import time
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = os.getenv("SPOTIFY_RANDIE_BOT_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_RANDIE_BOT_CLIENT_SECRET")

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# toggle theatrical mode
IN_THEATRICAL_MODE = False


def toggle_sleep(in_theatrical_mode):
    if in_theatrical_mode:
        time.sleep(1)


def welcome_dialogue():
    print("Starting up services...")
    toggle_sleep(IN_THEATRICAL_MODE)
    print("Authenticating with Spotify...")
    toggle_sleep(IN_THEATRICAL_MODE)
    print("Waking Randie up...")
    toggle_sleep(IN_THEATRICAL_MODE)


welcome_dialogue()
available_genres = spotify.recommendation_genre_seeds()["genres"]


def print_available_genres():
    for genre in available_genres:
        print("- " + genre)


print("Please specify a genre (For a list of available genres type '-list or --l').")
command = input("Genre: ")

while command not in available_genres:

    if command == "exit":
        break

    if command == "-list" or command == "--l":
        print_available_genres()
    else:
        print("Genre '" + command + "' is invalid. Please ty again or type 'exit' to go back.")
    command = input("Genre: ")

selected_genre = command
print("Selected genre is: ", selected_genre)
