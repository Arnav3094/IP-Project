import create
from create import *

df = create.df
mean_df = create.mean_df
df_sorted_liveness = df.sort_values(by=['liveness'], ascending=False)
mean_df_sorted_liveness = mean_df.sort_values(by=['liveness'], ascending=False)
df_sorted_liveness.liveness *= 100
mean_df_sorted_liveness *= 100

py.figure(dpi=450)
py.hist(df_sorted_liveness.liveness, bins=range(0, 105, 5), rwidth=0.7, color='#C86A72')
py.axis(xmin=-1, xmax=101, ymax=325)
ax = py.gca()
py.xticks(range(0, 105, 5), fontsize=8)
py.yticks(range(0, 350, 25))
ax.yaxis.set_ticks_position('both')
ax.xaxis.set_ticks_position('both')
ax.yaxis.set_minor_locator(AutoMinorLocator())
py.grid()
py.title("Distribution of Liveness")
py.xlabel("Liveness (out of 100)")
py.ylabel("Number of Tracks")
py.savefig('liveness_hist')
py.close()

x1 = range(5, 105, 10)
py.figure(dpi=450)
py.bar(x1, df_sorted_liveness.liveness.iloc[0:10], width=5, color='#CB522E')
names = list(df_sorted_liveness.name.iloc[0:10])
py.axis(ymin=75, ymax=95)
names_new = []
for name in names:
    words = name.split(" ")
    names_new.append([" ".join(words[i:i + 1]) for i in range(0, len(words), 1)])
for name in names_new:
    names_new[names_new.index(name)] = str.join("\n", name)
py.xticks(x1, names_new, fontsize=6)
py.title("Songs with the Highest Liveness")
py.ylabel("Liveness (out of 100)")
py.grid(axis='y')
ax = py.gca()
ax.yaxis.set_ticks_position('both')
ax.yaxis.set_minor_locator(AutoMinorLocator())
py.savefig('liveness_bar_top10')
py.close()

py.figure(dpi=450)
py.bar(x1, mean_df_sorted_liveness.liveness.iloc[0:10], width=5, color='#00A995')
artists = list(mean_df_sorted_liveness.iloc[0:10, 1:2].index)
try: artists[artists.index("Joey Bada$$")] = "Joey Badass"
except ValueError: pass
except Exception as e: print(e)
artists_new = []
for artist in artists:
    words = artist.split(" ")
    artists_new.append([" ".join(words[i:i + 1]) for i in range(0, len(words), 1)])
for artist in artists_new: artists_new[artists_new.index(artist)] = str.join("\n", artist)
py.xticks(x1, artists_new, fontsize=7)
py.title("Artists with the Highest Liveness")
py.ylabel("Liveness (out of 100)")
py.axis(ymin=27.5, ymax=37.5)
py.yticks(np.array(range(55, 76, 5))/2)
py.grid(axis='y', which='major')
py.grid(axis='y', which='minor', linewidth=0.3)
ax = py.gca()
ax.yaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_ticks_position('both')
ax.yaxis.set_minor_formatter(ScalarFormatter())
ax.tick_params(which='minor', axis='y', labelsize=7)
py.savefig('liveness_bar_artists_top10')
py.close()
