import create
from create import *

df = create.df
mean_df = create.mean_df
df_sorted_loudness = df.sort_values(by=['loudness'], ascending=False)
mean_df_sorted_loudness = mean_df.sort_values(by=['loudness'], ascending=False)

py.figure(dpi=450)
py.hist(df_sorted_loudness.loudness, bins=range(-23, 0, 1), rwidth=0.7, color='#51A063')
py.plot()
py.plot()
py.axis(xmax=0, xmin=-23)
ax = py.gca()
ax.yaxis.tick_right()
ax.yaxis.set_ticks_position('both')
ax.yaxis.set_minor_locator(AutoMinorLocator())
ax.xaxis.set_minor_locator(AutoMinorLocator())
py.grid()
py.title("Distribution of Loudness")
py.xlabel("Loudness")
py.ylabel("Number of Tracks")
py.savefig('loudness_hist')
py.close()

x1 = range(5, 105, 10)
py.figure(dpi=450, figsize=(9, 5))
py.bar(x1, df_sorted_loudness.loudness.iloc[0:10], width=5, )
names = list(df_sorted_loudness.name.iloc[0:10])
py.yticks(np.array(range(-10, 1)) / 4)
py.axis(ymax=0, ymin=-2.5)
names_new = []
for name in names:
    words = name.split(" ")
    names_new.append([" ".join(words[i:i + 2]) for i in range(0, len(words), 2)])
for name in names_new:
    names_new[names_new.index(name)] = str.join("\n", name)
py.xticks(x1, names_new, fontsize=6.5)
py.title("Loudest Songs")
py.ylabel("Loudness")
py.grid(axis='y')
py.savefig('loudness_bar_top10')
py.close()

py.figure(dpi=450, figsize=(8, 5))
py.bar(x1, mean_df_sorted_loudness.loudness.iloc[0:10], width=5, color='#FF005D')
artists = mean_df_sorted_loudness.iloc[0:10, 1:2].index
py.xticks(x1, artists, fontsize=6.5)
py.title("Loudest Artists")
py.ylabel("Loudness")
py.yticks(np.array(range(-20, -13)) / 4)
py.grid(axis='y')
py.axis(ymin=-4.75, ymax=-3.5)
ax = py.gca()
ax.yaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_ticks_position('both')
ax.yaxis.set_minor_locator(AutoMinorLocator())
py.savefig('loudness_bar_artists_top10')
py.close()
