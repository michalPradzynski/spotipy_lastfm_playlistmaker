import secrets
import spotipy
from spotipy.oauth2 import SpotifyOAuth


class PlaylistMaker:
    def __init__(self, playlist_name):
        self.playlist_name = playlist_name
        self._scope = "user-library-read,playlist-modify-public"

        self.sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id=secrets.SPOTIPY_CLIENT_ID,
                client_secret=secrets.SPOTIPY_CLIENT_SECRET,
                redirect_uri=secrets.SPOTIPY_REDIRECT_ID,
                scope=self._scope
            )
        )

    def get_artist(self, name) -> dict | None:
        results = self.sp.search(q='artist:' + name, type='artist')
        items = results['artists']['items']
        if len(items) > 0:
            return items[0]
        else:
            return None

    def get_artists_top_5(self, artist: str) -> dict[str:str]:
        results = self.sp.artist_top_tracks(artist["id"])
        top_5 = {track["id"]: track["name"] for track in results['tracks'][:5]}
        return top_5

    def create_playlist(self) -> dict:
        user_id = self.sp.me()["id"]
        playlist = self.sp.user_playlist_create(user_id, self.playlist_name)
        return playlist

    def add_tracks_to_playlist(self, playlist_id: str, tracks_ids: list[str]) -> None:
        self.sp.playlist_add_items(playlist_id, tracks_ids)
