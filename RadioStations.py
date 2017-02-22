import urllib
from bs4 import BeautifulSoup
import json
import re
import ast

# Differences: urllib.urlopen to urllib.request.urllopen, print to print()

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
jack_url = urllib.request.urlopen(jack).read()
jack = BeautifulSoup(jack_url, "lxml")
songs = jack.findAll(attrs={"class":"playlist-item"})
jack_songs = []
for i in songs:
    song_name = i.get("data-title", "NULL")
    artist_name = i.get("data-artist", "NULL")
    time = i.findAll(attrs={"class":"time"})[0].string
    
    oneList = [song_name, artist_name, time]
    jack_songs.append(oneList)
print(jack_songs)
'''

# Kool 108
'''
kool_address = "http://kool108.iheart.com/music/recently-played/"
kool_url = urllib.request.urlopen(kool_address).read()
kool = BeautifulSoup(kool_url, "lxml")
songs = kool.findAll(attrs={"class":"playlist-track-container"})
kool_songs = []
for i in songs:
    song_name = i.findAll(attrs={"class":"track-title station-custom-link-hover"})[0].string
    artist_name = i.findAll(attrs={"class":"track-artist station-custom-link-hover"})[0].string
    time = i.findAll('span')[0].find(text = True)
    
    oneList = [song_name, artist_name, time]
    kool_songs.append(oneList)
print(kool_songs)
'''

# K102
'''
k102_address = "http://k102.iheart.com/music/recently-played/"
k102_url = urllib.request.urlopen(k102_address).read()
k102 = BeautifulSoup(k102_url, "lxml")
songs = k102.findAll(attrs={"class":"playlist-track-container"})
k102_songs = []
for i in songs:
    song_name = i.findAll(attrs={"class":"track-title station-custom-link-hover"})[0].string
    artist_name = i.findAll(attrs={"class":"track-artist station-custom-link-hover"})[0].string
    time = i.findAll('span')[0].find(text = True)
    
    oneList = [song_name, artist_name, time]
    k102_songs.append(oneList)
    
print(k102_songs)
'''

# BUZ'N
'''
buzn = "http://buzn1029.cbslocal.com/playlist/"
buzn_url = urllib.request.urlopen(buzn).read()
buzn = BeautifulSoup(buzn_url, "lxml")
songs = buzn.findAll(attrs={"class":"playlist-item"})
buzn_songs = []
for i in songs:
    song_name = i.get("data-title", "NULL")
    artist_name = i.get("data-artist", "NULL")
    time = i.findAll(attrs={"class":"time"})[0].string
    
    oneList = [song_name, artist_name, time]
    buzn_songs.append(oneList)
print(buzn_songs)
'''

# The Current
'''
current_address = "http://www.thecurrent.org/playlist"
current_url = urllib.request.urlopen(current_address).read()
current = BeautifulSoup(current_url, "lxml")

songs = current.findAll(attrs={"class":"row song"})

current_songs = []
for i in songs:
    song_name = i.findAll(attrs={"class":"title"})[0].find(text=True).strip()
    artist_name = i.findAll(attrs={"class":"artist"})[0].string.strip()
    time = i.findAll("time")[0].string.strip()
    
    oneList = [song_name, artist_name, time]
    current_songs.append(oneList)
    
print(current_songs)
'''

# KQRS
'''
kqrs_address = "http://kqrs.tunegenie.com/onair/"
kqrs_url = urllib.request.urlopen(kqrs_address).read()
kqrs = BeautifulSoup(kqrs_url, "lxml")

songs = kqrs.findAll(attrs={"class":"slot lt"})

i = songs[1]

a = i.findAll("div")[4].string.strip("\*")
b = i.findAll("div")[5].find(text=True).replace(" VINYL", "")
c = i.findAll(attrs={"class":"timestamp"})[0].string
              
kqrs_songs = []
for i in songs:
    song_name = i.findAll("div")[4].string.strip("\*")
    artist_name = i.findAll("div")[5].find(text=True).replace(" VINYL", "")
    time = i.findAll(attrs={"class":"timestamp"})[0].string

    oneList = [song_name, artist_name, time]
    kqrs_songs.append(oneList)
              
print(kqrs_songs)
'''

# KTIS Not Working
ktis_address = "http://myktis.com/recently-played/"
ktis_url = urllib.request.urlopen(ktis_address).read()
ktis = BeautifulSoup(ktis_url, "lxml")

songs = ktis.findAll(attrs={"class":"artistsongcontainer"})
 
ktis_songs = []
for i in songs:
    song_name = i.findAll(attrs={"class":"songname"})[0].a.string
    artist_name = i.findAll(attrs={"class":"artistname"})[0].string
    #time = i.findAll(attrs={"class":"timeplayed"})[0].string
        
    oneList = [song_name, artist_name]
    ktis_songs.append(oneList)
print(ktis_songs)


# Refuge Radio 91.5
