import urllib
from bs4 import BeautifulSoup
import json
import re
import ast

# Differences: urllib.urlopen to urllib.request.urllopen, print to print()

# Cities 97
# 10 songs, time
# ~30 min
'''
cities97 = "http://cities97.iheart.com/music/recently-played/"
cities97_url = urllib.request.urlopen(cities97).read()
c97 = BeautifulSoup(cities97_url, "lxml")
songs = c97.findAll(attrs={"class":"playlist-track-container"})
cities97_songs = []
for i in songs:
    song_name = i.findAll(attrs={"class":"track-title station-custom-link-hover"})[0].string
    artist_name = i.findAll(attrs={"class":"track-artist station-custom-link-hover"})[0].string
    time = i.findAll('span')[0].find(text = True)
    
    oneList = [song_name, artist_name, time]
    cities97_songs.append(oneList)
print(cities97_songs)
'''

# KDWB
# 10 songs, time
# ~40 min
'''
kdwb = "http://kdwb.iheart.com/music/recently-played/"
kdwb_url = urllib.request.urlopen(kdwb).read()
kdwb = BeautifulSoup(kdwb_url, "lxml")
songs = kdwb.findAll(attrs={"class":"playlist-track-container"})
kdwb_songs = []
for i in songs:
    song_name = i.findAll(attrs={"class":"track-title station-custom-link-hover"})[0].string
    artist_name = i.findAll(attrs={"class":"track-artist station-custom-link-hover"})[0].string
    time = i.findAll('span')[0].find(text = True)
    
    oneList = [song_name, artist_name, time]
    kdwb_songs.append(oneList)
print(kdwb_songs)
'''

# Go 96.3
# 30 songs, timstamp milliseconds
# ~1:50
'''
g96 = "http://player.listenlive.co/31261/en/songhistory"
g96_url = urllib.request.urlopen(g96).read()
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
print(g96_songs)
'''

# Jack FM
# All songs that day, time
# Could just scrape after the fact
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
# 10 songs, time
# ~30 min
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
# 10 songs, time
# ~30 min
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
# All songs that day, time
# Could just scrape after the fact
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
# All songs that day, time
# Could just scrape after the fact
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
# 30 songs, time milliseconds
# ~2:20
'''
kqrs_address = "http://kqrs.tunegenie.com/onair/"
kqrs_url = urllib.request.urlopen(kqrs_address).read()
kqrs = BeautifulSoup(kqrs_url, "lxml")

songs = kqrs.findAll(attrs={"class":"slot lt"})

kqrs_songs = []
for i in songs:
    song_name = i.findAll("div")[4].string.strip("\*")
    artist_name = i.findAll("div")[5].find(text=True).replace(" VINYL", "")
    time = i.findAll(attrs={"class":"timestamp"})[0].string

    oneList = [song_name, artist_name, time]
    kqrs_songs.append(oneList)
              
print(kqrs_songs)
'''

# KTIS
'''
ktis_address = "http://myktis.com/recently-played/"
ktis_url = urllib.request.urlopen(ktis_address).read()
ktis = BeautifulSoup(ktis_url, "lxml")

songs = ktis.findAll(attrs={"class":"artistsongcontainer"})
 
ktis_songs = []

sl = 0

for i in songs:
    song_name = i.findAll(attrs={"class":"songname"})[0].a.string
    artist_name = i.findAll(attrs={"class":"artistname"})[0].string
    #time = i.findAll(attrs={"class":"timeplayed"})[0].string
        
    oneList = [song_name, artist_name]
    ktis_songs.append(oneList)
    
    sl += 1


times = ktis.findAll(attrs={"class":"time"})

ktis_times = []
tl = 0
for i in times:
    ktis_times.append(i.string)
    
    tl += 1
    

for i in range(len(ktis_songs)):
    ktis_songs[i].append(ktis_times[i])
    
print(ktis_songs)
'''

# 93x
'''
kxxr_address = "http://kxxr.tunegenie.com/"
kxxr_url = urllib.request.urlopen(kxxr_address).read()
kxxr = BeautifulSoup(kxxr_url, "lxml")

songs = kxxr.findAll(attrs={"class":"slot lt"})
              
kxxr_songs = []
for i in songs:
    song_name = i.findAll("div")[4].string.strip("\*")
    artist_name = i.findAll("div")[5].find(text=True).replace(" VINYL", "")
    time = i.findAll(attrs={"class":"timestamp"})[0].string

    oneList = [song_name, artist_name, time]
    kxxr_songs.append(oneList)
              
print(kxxr_songs)
'''

# Go 96.3
'''
g95 = "http://player.listenlive.co/47141/en/songhistory"
g95_url = urllib.request.urlopen(g95).read()
g95 = BeautifulSoup(g95_url, "lxml")
songs_js = g95.findAll("script")[15].string
songs_json = re.search("\[\{.*\]", songs_js).group()
songs_dict_list = ast.literal_eval(songs_json)
g95_songs = []
for i in songs_dict_list:
	song_name = i["title"]
	artist_name = i["artist"]
	time = i["timestamp"]
	oneList = [song_name, artist_name, time]
	g95_songs.append(oneList)
print(g95_songs)
'''

# Hot 102.5
'''
h102_address = "http://hot1025.iheart.com/music/playlist/"
h102_url = urllib.request.urlopen(h102_address).read()
h102 = BeautifulSoup(h102_url, "lxml")
songs = h102.findAll(attrs={"class":"playlist-track-container"})
h102_songs = []
for i in songs:
    song_name = i.findAll(attrs={"class":"track-title station-custom-link-hover"})[0].string
    artist_name = i.findAll(attrs={"class":"track-artist station-custom-link-hover"})[0].string
    time = i.findAll('span')[0].find(text = True)
    
    oneList = [song_name, artist_name, time]
    h102_songs.append(oneList)
    
print(h102_songs)
'''


# The Vibe 105
# KS95
# Refuge Radio 91.5
# BOB Country 106.1










