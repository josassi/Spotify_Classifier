import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd

scope = "playlist-read-private,user-read-private,playlist-read-collaborative,user-library-read"
username = "josass1"
client_id = "e8d821f241b2408baef01dbf9296a36d"
client_secret = "851229608a314367818738d87e532ee4"
uri = "http://localhost:8040"

oauth_manager = SpotifyOAuth(client_id=client_id,
                             client_secret=client_secret,
                             redirect_uri=uri,
                             state=None,
                             scope=scope,
                             cache_path=None,
                             username=None,
                             proxies=None,
                             show_dialog=True,
                             requests_timeout=None)

sp = spotipy.Spotify(oauth_manager=oauth_manager)

df_features = pd.DataFrame(sp.categories(country="FR", limit=50)["categories"]["items"])
print(df_features)