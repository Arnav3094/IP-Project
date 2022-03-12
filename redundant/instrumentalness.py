import create
from create import *

df = create.df
mean_df = create.mean_df
df_sorted_instrumentalness = df.sort_values(by=['instrumentalness'], ascending=False)
mean_df_sorted_instrumentalness = mean_df.sort_values(by=['instrumentalness'], ascending=False)
df_sorted_instrumentalness.instrumentalness *= 100
mean_df_sorted_instrumentalness *= 100

py.figure(dpi=450, figsize=(6, 7))
py.hist(df_sorted_instrumentalness.instrumentalness, bins=range(0, 105, 5), rwidth=0.7, color='#A90036')
py.axis(xmin=-1, xmax=101)
ax = py.gca()
py.yscale('log')
ax.yaxis.set_ticks_position('both')
ax.xaxis.set_ticks_position('both')
py.grid()
py.title("(Logarithmic) Distribution of Instrumentalness")
py.xlabel("Instrumentalness")
py.ylabel("Number of Tracks")
py.savefig('instrumentalness_log_hist')
py.close()

x1 = range(5, 105, 10)
py.figure(dpi=450, figsize=(7, 5))
py.bar(x1, df_sorted_instrumentalness.instrumentalness.iloc[0:10], width=5, color='#C4C82F')
names = list(df_sorted_instrumentalness.name.iloc[0:10])
py.axis(ymin=80, ymax=95)
py.yticks(range(80, 96))
names_new = []
for name in names:
    words = name.split(" ")
    names_new.append([" ".join(words[i:i + 2]) for i in range(0, len(words), 2)])
for name in names_new:
    names_new[names_new.index(name)] = str.join("\n", name)
py.xticks(x1, names_new, fontsize=6)
py.title("Songs with the Highest Instrumentalness")
py.ylabel("Instrumentalness (out of 100)")
py.grid(axis='y')
ax = py.gca()
ax.yaxis.set_ticks_position('both')
ax.yaxis.set_minor_locator(AutoMinorLocator())
py.savefig('instrumentalness_bar_top10')
py.close()

py.figure(dpi=450)
py.bar(x1, mean_df_sorted_instrumentalness.instrumentalness.iloc[0:10], width=5, color='#75C883')
artists = list(mean_df_sorted_instrumentalness.iloc[0:10, 1:2].index)
py.yscale('log')
try: artists[artists.index("Joey Bada$$")] = "Joey Badass"
except ValueError: pass
except Exception as e: print(e)
artists_new = []
for artist in artists:
    words = artist.split(" ")
    artists_new.append([" ".join(words[i:i + 1]) for i in range(0, len(words), 1)])
for artist in artists_new: artists_new[artists_new.index(artist)] = str.join("\n", artist)
py.xticks(x1, artists_new, fontsize=7)
py.title("Artists with the Highest Instrumentalness (Logarithmic)")
py.ylabel("Instrumentalness (out of 100)")
py.axis(ymin=5, ymax=81)
py.grid(axis='y', which='major')
py.grid(axis='y', which='minor', linewidth=0.3)
ax = py.gca()
ax.yaxis.set_minor_formatter(ScalarFormatter())
ax.yaxis.set_major_formatter(ScalarFormatter())
ax.yaxis.set_ticks_position('both')
py.savefig('instrumentalness_log_bar_artists_top10')
py.close()
