import calendar
import secrets
from datetime import datetime

from lastfm_scrapper import LastfmScrapper
from spotipy_playlistmaker import PlaylistMaker


scrapper = LastfmScrapper(username=secrets.LASTFM_USERNAME, password=secrets.LASTFM_PASSWORD)
driver = scrapper.driver
print("Scrapping recommended artists list from Last.fm")
driver.get("https://www.last.fm/login")
driver.implicitly_wait(1)
scrapper.cookies_rejecter()
scrapper.login()
driver.implicitly_wait(1)
recommended_artists = scrapper.get_recommended_artists()

year = datetime.now().year
month = calendar.month_name[datetime.now().month]
pm = PlaylistMaker(playlist_name=f"My Last.fm recommendations - {month} {year}")

print("Creating a new playlist")
playlist_id = pm.create_playlist()["id"]

print("Getting artists info from Spotify")
for artist in recommended_artists:
    artist_info = pm.get_artist(artist)
    if artist_info:
        top_5_tracks = list(pm.get_artists_top_5(artist_info).keys())
        print(f"Adding Top 5 tracks of {artist} to the playlist")
        pm.add_tracks_to_playlist(playlist_id=playlist_id, tracks_ids=top_5_tracks)
    else:
        print("Can't find that artist", artist)

print("All done. Happy listening :)")
