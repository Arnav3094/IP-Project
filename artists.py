import main

artists = main.artists.copy()
artists.sort(key=str.lower)
print(artists)
