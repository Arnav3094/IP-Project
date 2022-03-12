import create
from create import *

df = create.df
mean_df = create.mean_df
df_sorted_valence = df.sort_values(by=['valence'], ascending=False)
mean_df_sorted_valence = mean_df.sort_values(by=['valence'], ascending=False)
df_sorted_valence.valence *= 100
mean_df_sorted_valence *= 100

py.figure(dpi=450)
py.hist(df_sorted_valence.valence, bins=range(0, 105, 5), rwidth=0.7, color='#C86A72')
py.axis(xmin=-1, xmax=101, ymax=90)
ax = py.gca()
py.xticks(range(0, 105, 5), fontsize=8)
ax.yaxis.set_ticks_position('both')
ax.yaxis.set_minor_locator(AutoMinorLocator())
py.grid()
py.title("Distribution of Valence")
py.xlabel("Valence (out of 100)")
py.ylabel("Number of Tracks")
py.savefig('valence_hist')
py.close()

x1 = range(5, 105, 10)
py.figure(dpi=450)
py.bar(x1, df_sorted_valence.valence.iloc[0:10], width=5, color='#C80045')
names = list(df_sorted_valence.name.iloc[0:10])
py.axis(ymin=96, ymax=97.5)
py.yticks([96, 96.25, 96.5, 96.75, 97, 97.25, 97.5])
names_new = []
for name in names:
    words = name.split(" ")
    names_new.append([" ".join(words[i:i + 1]) for i in range(0, len(words), 1)])
for name in names_new:
    names_new[names_new.index(name)] = str.join("\n", name)
py.xticks(x1, names_new, fontsize=6)
py.title("Songs with the Highest Valence")
py.ylabel("Valence (out of 100)")
py.grid(axis='y')
ax = py.gca()
ax.yaxis.set_ticks_position('both')
ax.yaxis.set_minor_locator(AutoMinorLocator())
py.savefig('valence_bar_top10')
py.close()

py.figure(dpi=450)
py.bar(x1, mean_df_sorted_valence.valence.iloc[0:10], width=5, color='#00A995')
artists = list(mean_df_sorted_valence.iloc[0:10, 1:2].index)
try: artists[artists.index("Joey Bada$$")] = "Joey Badass"
except ValueError: pass
except Exception as e: print(e)
artists_new = []
for artist in artists:
    words = artist.split(" ")
    artists_new.append([" ".join(words[i:i + 1]) for i in range(0, len(words), 1)])
for artist in artists_new: artists_new[artists_new.index(artist)] = str.join("\n", artist)
py.xticks(x1, artists_new, fontsize=7)
py.title("Artists with the Highest Valence")
py.ylabel("Valence (out of 100)")
py.axis(ymin=65, ymax=77)
py.yticks(range(65, 78))
py.grid(axis='y', which='major')
ax = py.gca()
ax.yaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_ticks_position('both')
py.savefig('valence_bar_artists_top10')
py.close()
