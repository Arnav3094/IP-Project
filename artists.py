import create
from create import *

print(len(pd.Series(create.artists).unique()))
print(len(create.artists))

artists = create.artists.copy()
artists.sort(key=str.lower)
print(artists)
