import time
import schedule
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Replace these with your own credentials
client_id = '20c107e779e04e20a693a24157e63262'
client_secret = '8f5e39d15bcb4a1e8780be3b4dd40b3b'
redirect_uri = 'http://localhost:5000/callback'
playlist_uri = 'spotify:playlist:37i9dQZF1DXa1rZf8gLhyz'

# Set up Spotify API authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope='user-read-playback-state user-modify-playback-state'))

def start_spotify_playback():
    # Get a list of available devices
    devices = sp.devices()

    if devices['devices']:
        # Choose the first available device
        device_id = devices['devices'][0]['id']

        # Start playback on the selected device, in shuffle mode
        sp.start_playback(device_id=device_id, context_uri=playlist_uri, shuffle=True)
        print("Playlist will start playing on device:", devices['devices'][0]['name'])
    else:
        print("No active devices found.")

def stop_spotify_playback():
    # Stop playback on all devices
    sp.pause_playback()
    print("Playback stopped.")

# Schedule the playback job at 8:30 pm
schedule.every().day.at("20:30").do(start_spotify_playback)

# Schedule the stop job at 8:00 am
schedule.every().day.at("08:00").do(stop_spotify_playback)

# Run the schedule loop
while True:
    schedule.run_pending()
    time.sleep(1)
