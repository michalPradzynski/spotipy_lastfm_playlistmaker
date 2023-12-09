# spotipy_lastfm_playlistmaker
One-day project for scrapping first 20 recommended artists from my Last.fm and creating a playlist with their Top 5 tracks on Spotify.

This script logs on Last.fm, goes to Recommended artists page and scraps the first 20 of them with the help of Selenium, because Last.fm API does not provide such data.
Then, with the help of Spotipy, the script looks through those artists' TOP 5 tracks from US and creates a playlist with those tracks.

Maybe someday I'll upgrade it to make it do more. Maybe I'll write some tests for it. You know how such projects work :)
