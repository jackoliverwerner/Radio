# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 14:07:02 2017

@author: jack.werner1
"""

#%%
import urllib
from bs4 import BeautifulSoup

cities97 = "http://cities97.iheart.com/music/recently-played/"

cities97_url = urllib.request.urlopen(cities97).read()
c97 = BeautifulSoup(cities97_url, "lxml")

songs = c97.findAll(attrs={"class":"playlist-track-container"})
#%%

songList = []

for i in songs:
    song_name = i.findAll(attrs={"class":"track-title station-custom-link-hover"})[0].string
    artist_name = i.findAll(attrs={"class":"track-artist station-custom-link-hover"})[0].string
    time = i.findAll('span')[0].find(text = True)
    
    oneList = [song_name, artist_name, time]

    songList.append(oneList)
#%%