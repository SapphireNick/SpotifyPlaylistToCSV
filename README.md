# SpotifyPlaylistToCSV

This python script does exactly as the name suggests.
Given the id of any Spotify-Playlist the script converts the playlist into a .csv file. The csv file contains the Song-Name, Artist-Name, Album-Name, Duration and the Spotify-URL to each song in the playlist.

## <b>Usage</b>

To make the script as easy to understand and transparent as possible a personal Spoitfy-App has to be created which includes the Client-ID and Client-Secret used for the query.
Instructions on how to create a Spotify-App can be found here: https://developer.spotify.com/documentation/general/guides/authorization/app-settings/

After a Client-ID and Client-Secret have been aquired one can start the script by using:

```console
python SpotifyPlaylistToCSV.py
```

Enter the Client-ID and Client-Secret. Afterwards enter the ID of the playlist which can be found in the URL to the playlist.
