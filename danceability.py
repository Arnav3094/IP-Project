import create
from create import *

df = create.df
mean_df = create.mean_df
df_sorted_danceability = df.sort_values(by=['danceability'], ascending=False)
mean_df_sorted_danceability = mean_df.sort_values(by=['danceability'], ascending=False)
df_sorted_danceability.danceability *= 100
mean_df_sorted_danceability *= 100


py.figure(dpi=450)
py.hist(df_sorted_danceability.danceability, bins=range(15, 105, 5), rwidth=0.7, color='#A73E0C')
py.axis(xmin=15, xmax=101)
ax = py.gca()
py.xticks(range(15, 105, 5), fontsize=8)
py.yticks(range(0, 200, 25))
ax.yaxis.set_ticks_position('both')
ax.xaxis.set_ticks_position('both')
ax.yaxis.set_minor_locator(AutoMinorLocator())
py.grid()
py.title("Distribution of Danceability")
py.xlabel("Danceability (out of 100)")
py.ylabel("Number of Tracks")
py.savefig('danceability_hist')
py.close()

x1 = range(5, 105, 10)
py.figure(dpi=450, figsize=(7, 5))
py.bar(x1, df_sorted_danceability.danceability.iloc[0:10], width=5, color='#CB522E')
names = list(df_sorted_danceability.name.iloc[0:10])
py.axis(ymin=90, ymax=100)
py.yticks(range(90, 101))
names_new = []
for name in names:
    words = name.split(" ")
    names_new.append([" ".join(words[i:i + 2]) for i in range(0, len(words), 2)])
for name in names_new:
    names_new[names_new.index(name)] = str.join("\n", name)
py.xticks(x1, names_new, fontsize=6)
py.title("Songs with the Highest Danceability")
py.ylabel("Danceability (out of 100)")
py.grid(axis='y')
ax = py.gca()
ax.yaxis.set_ticks_position('both')
ax.yaxis.set_minor_locator(AutoMinorLocator())
py.savefig('danceability_bar_top10')
py.close()

py.figure(dpi=450)
py.bar(x1, mean_df_sorted_danceability.danceability.iloc[0:10], width=5, color='#00A995')
artists = list(mean_df_sorted_danceability.iloc[0:10, 1:2].index)
try: artists[artists.index("Joey Bada$$")] = "Joey Badass"
except ValueError:
    pass
except Exception as e:
    print(e)
artists_new = []
for artist in artists:
    words = artist.split(" ")
    artists_new.append([" ".join(words[i:i + 1]) for i in range(0, len(words), 1)])
for artist in artists_new:
    artists_new[artists_new.index(artist)] = str.join("\n", artist)
py.xticks(x1, artists_new, fontsize=7)
py.title("Artists with the Highest Danceability")
py.ylabel("Danceability (out of 100)")
py.axis(ymin=75, ymax=87.5)
py.yticks(np.linspace(75, 87.5, 11))
py.grid(axis='y')
ax = py.gca()
ax.yaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_ticks_position('both')
py.savefig('danceability_bar_artists_top10')
py.close()
