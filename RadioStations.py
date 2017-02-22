
import urllib
from bs4 import BeautifulSoup
import json
import re
import ast

# Cities 97
'''
cities97 = "http://cities97.iheart.com/music/recently-played/"

cities97_url = urllib.urlopen(cities97).read()

c97 = BeautifulSoup(cities97_url, "lxml")

songs = c97.findAll(attrs={"class":"playlist-track-container"})

cities97_songs = []

for i in songs:
    song_name = i.findAll(attrs={"class":"track-title station-custom-link-hover"})[0].string
    artist_name = i.findAll(attrs={"class":"track-artist station-custom-link-hover"})[0].string
    time = i.findAll('span')[0].find(text = True)
    
    oneList = [song_name, artist_name, time]

    cities97_songs.append(oneList)

print cities97_songs
'''

# KDWB
'''
kdwb = "http://kdwb.iheart.com/music/recently-played/"

kdwb_url = urllib.urlopen(kdwb).read()

kdwb = BeautifulSoup(kdwb_url, "lxml")

songs = kdwb.findAll(attrs={"class":"playlist-track-container"})

kdwb_songs = []

for i in songs:
    song_name = i.findAll(attrs={"class":"track-title station-custom-link-hover"})[0].string
    artist_name = i.findAll(attrs={"class":"track-artist station-custom-link-hover"})[0].string
    time = i.findAll('span')[0].find(text = True)
    
    oneList = [song_name, artist_name, time]

    kdwb_songs.append(oneList)

print kdwb_songs
'''

# Go 96.3
'''
g96 = "http://player.listenlive.co/31261/en/songhistory"

g96_url = urllib.urlopen(g96).read()

g96 = BeautifulSoup(g96_url, "lxml")

songs_js = g96.findAll("script")[15].string

songs_json = re.search("\[\{.*\]", songs_js).group()

songs_dict_list = ast.literal_eval(songs_json)

g96_songs = []

for i in songs_dict_list:
	song_name = i["title"]
	artist_name = i["artist"]
	time = i["timestamp"]

	oneList = [song_name, artist_name, time]

	g96_songs.append(oneList)

print g96_songs
'''

# Jack FM
'''
jack = "http://1041jackfm.cbslocal.com/playlist/"

jack_url = urllib.urlopen(jack).read()

jack = BeautifulSoup(jack_url, "lxml")

songs = jack.findAll(attrs={"class":"playlist-item"})

jack_songs = []

for i in songs:
    song_name = i.get("data-title", "NULL")
    artist_name = i.get("data-artist", "NULL")
    time = i.findAll(attrs={"class":"time"})[0].string
    
    oneList = [song_name, artist_name, time]

    jack_songs.append(oneList)

print jack_songs
'''









