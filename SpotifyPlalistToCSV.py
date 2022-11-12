import requests
import json
import csv
import base64
from datetime import date

client_id = input("Client ID: ")
client_secret = input("Client Secret: ")
msg = f"{client_id}:{client_secret}"
msgBytes = msg.encode('ascii')
base64Bytes = base64.b64encode(msgBytes)
base64Msg = base64Bytes.decode('ascii')

token_headers = {
    'Authorization': 'Basic ' + base64Msg
}

token_data = {
    'grant_type': 'client_credentials'
}

res_token = requests.post('https://accounts.spotify.com/api/token', headers=token_headers, data=token_data)
token = json.loads(res_token.text)["access_token"]

filename = "export" + str(date.today()) + ".csv"

file = open(filename, "w")
writer = csv.writer(file)
writer.writerow(["Song","Artist","Album","Duration","Url"])

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + token,
}

playlist_id = input("PlaylistID: ")
next = 'https://api.spotify.com/v1/playlists/' + playlist_id + '/tracks?offset=0&limit=100'

while next != None:
    response = requests.get(next, headers=headers)

    tracks = json.loads(response.text)["items"]

    for track in tracks:
        song = track["track"]
        line = []
        line.append(song["name"])

        artists = song["artists"]
        artist_list = ""
        for artist in artists:
            artist_list += artist["name"] + ","
        # remove last comma
        artist_list = artist_list[:-1]

        line.append(artist_list)
        line.append(song["album"]["name"])

        duration = song["duration_ms"]
        seconds = int((duration/(1000))%60)
        if seconds<10:
            seconds_str = "0" + str(seconds)
        else:
            seconds_str = str(seconds)
        line.append(str(int((duration/(1000*60))%60)) + ":" + seconds_str)

        if len(song["external_urls"])!=0:
            line.append(song["external_urls"]["spotify"])

        writer.writerow(line)

    next = json.loads(response.text)["next"]

