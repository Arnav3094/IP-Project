from Base_SpotifyAPI_Class import SpotifyAPI
from FeaturesSpotifyAPI_Class import *

import requests
import base64
import datetime as dt
from urllib.parse import urlencode
from pprint import pprint as pp

import pandas as pd
from pandas import DataFrame as DF
from pandas import Series as S
import numpy as np
import json
import time

from matplotlib import pyplot as py

client_id = '602ac06174344597a70ddd9949e97f50'
client_secret = '286a7572b3e944ff9708690eaaa4b8f2'

artists = []
artists += list(map(str, 'The Weeknd,Kanye West,Drake,Joyner,Lucas,Eminem,J. Cole,Kendrick Lamar,Logic,Meek Mill,50 Cent,Rihanna,Nicki Minaj,Cardi B,Travis Scott,Juice WRLD,Post Malone,Machine Gun Kelly,Closed on Sunday,Powfu,Kid Cudi,A$AP Rocky,Dr. Dre,2pac,The Notorious B.I.G.,JAY-Z,Pusha-T,Joey Bada$$,Hopsin,XXXTENTACION'.split(',')))
artists += list(map(str, 'Queen,The Beatles,Michael Jackson,Glass Animals,Taylor Swift,Imagine Dragons,Coldplay,Halsey,X Ambassadors,Hozier,The Chainsmokers,Avicii,Dj Snake,Martin Garrix,Skrillex,20syl,Kygo'.split(',')))
artists += list(map(str, 'Ed Sheeran,Bastille,Billie Eilish,Duncan Laurence,Dempsey Hope,Christian French,Miley Cyrus,Frank Ocean,Ellie Goulding,Camila Cabello,Alec Benjamin,Bruno Mars,Lauv,Selena Gomez,Maroon 5,Jon Bellion,JP Saxe,Alicia Keys,Ariana Grande,Justin Bieber,Anson Seabra,Justin Timberlake,Khalid,6LACK,Dean Lewis'.split(',')))
artists += list(map(str, 'One Direction,Katy Perry,Lady Gaga,Beyonce,Shawn Mendes,Sam Smith,Mac Miller,Linkin Park,Britney Spears,Alicia Keys,Black Eyed Peas,Green Day,Denzel Curry,AURORA,SZA,Lukas Graham'.split(',')))
artists += list(map(str, 'Bon Jovi,Sting,Backstreet Boys,Whitney Houston,David Bowie,AC/DC,Elvis Presley,Elton John,John Lennon,Bob Marley,ABBA,Paul McCartney'.split(',')))

if __name__ == '__main__':
    spotify = FeaturesSpotifyAPI(client_id, client_secret, artists)
    spotify.auth()
    spotify.get_artist_ids()
    spotify.get_top_tracks()
    spotify.get_top_track_features()
    spotify.get_combined()
    df = spotify.get_df()
    df.to_csv('music_data.csv')

df = pd.read_csv('music_data.csv')
mean_df = df.groupby("artist").mean()
mean_df.drop('Unnamed: 0', 1, inplace=True)
mean_df.to_csv('music_data_by_artist.csv')
