import create
from create import *

df = create.df
mean_df = create.mean_df
df_sorted_speechiness = df.sort_values(by=['speechiness'], ascending=False)
mean_df_sorted_speechiness = mean_df.sort_values(by=['speechiness'], ascending=False)
df_sorted_speechiness.speechiness *= 100
mean_df_sorted_speechiness *= 100

py.figure(dpi=450)
py.hist(df_sorted_speechiness.speechiness, bins=range(0, 56, 2), rwidth=0.7, color='#51A063')
py.axis(xmin=0, xmax=55, ymax=275)
ax = py.gca()
py.xticks(range(0, 56, 2), fontsize=8)
py.yticks(range(0, 300, 25))
ax.yaxis.set_ticks_position('both')
ax.yaxis.set_minor_locator(AutoMinorLocator())
py.grid()
py.title("Distribution of Speechiness")
py.xlabel("Speechiness")
py.ylabel("Number of Tracks")
py.savefig('speechiness_hist')
py.close()

x1 = range(5, 105, 10)
py.figure(dpi=450, figsize=(7, 5))
py.bar(x1, df_sorted_speechiness.speechiness.iloc[0:10], width=5, color='#5928A9')
names = list(df_sorted_speechiness.name.iloc[0:10])
py.axis(ymin=40, ymax=55)
py.yticks(range(40, 56))
names_new = []
for name in names:
    words = name.split(" ")
    names_new.append([" ".join(words[i:i + 2]) for i in range(0, len(words), 2)])
for name in names_new:
    names_new[names_new.index(name)] = str.join("\n", name)
py.xticks(x1, names_new, fontsize=6)
py.title("Songs with the Highest Speechiness")
py.ylabel("Speechiness")
py.grid(axis='y')
ax = py.gca()
ax.yaxis.set_ticks_position('both')
ax.yaxis.set_minor_locator(AutoMinorLocator())
py.savefig('speechiness_bar_top10')
py.close()

py.figure(dpi=450)
py.bar(x1, mean_df_sorted_speechiness.speechiness.iloc[0:10], width=5, color='#00A995')
artists = list(mean_df_sorted_speechiness.iloc[0:10, 1:2].index)
try: artists[artists.index("Joey Bada$$")] = "Joey Badass"
except Exception as e:
    if e is not ValueError:
        print(e)
artists_new = []
for artist in artists:
    words = artist.split(" ")
    artists_new.append([" ".join(words[i:i + 1]) for i in range(0, len(words), 1)])
for artist in artists_new:
    artists_new[artists_new.index(artist)] = str.join("\n", artist)
py.xticks(x1, artists_new, fontsize=7)
py.yticks(range(20, 33))
py.title("Artists with the Highest Speechiness")
py.ylabel("Speechiness")
py.axis(ymin=20, ymax=32)
py.grid(axis='y')
ax = py.gca()
ax.yaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_ticks_position('both')
py.savefig('speechiness_bar_artists_top10')
py.close()
