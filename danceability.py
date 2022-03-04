import create
from create import *

df = create.df
mean_df = create.mean_df
df_sorted_danceability = df.sort_values(by=['danceability'], ascending=False)
mean_df_sorted_danceability = mean_df.sort_values(by=['danceability'], ascending=False)

x = range(1, 1001)
py.figure(dpi=300)
py.bar(x, df_sorted_danceability.danceability, width=1)
ax = py.gca()
ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())
py.axis(ymin=0.2, xmin=-10, xmax=1010)
py.ylabel("Danceability of Song")
py.title("Distribution of Danceability")
py.grid()
py.savefig('danceability_bar')
py.close()

x1 = np.array(range(0, 100, 10))
x2 = x1 + 2
x3 = x1 + 1
py.figure(dpi=300)
py.bar(x1, df_sorted_danceability.danceability.iloc[0:10], width=2, label="Danceability")
py.bar(x2, (df_sorted_danceability.popularity/100).iloc[0:10], width=2, label="Popularity/100")
py.axis(ymin=0.75, ymax=0.975)
py.title("Danceability vs. Popularity of top 10 Most Danceable Tracks")
names_df = df.iloc[[int(y) for y in df_sorted_danceability.danceability.iloc[0:10].index], [3]]
names = list(names_df['name'])
names = [x if "(feat." not in x else x[:x.index("(") - 1]for x in names]
names.pop()
names.append("Another One Bites The Dust")
py.xticks(x1, names, fontsize=6, rotation=20)
py.legend(loc=1)
py.grid(axis='y')
py.savefig('danceability_bar_popularity_top10')
py.close()

py.figure(dpi=450)
py.bar(x1, df_sorted_danceability.danceability.iloc[-10:])
names = list((df.iloc[[int(y) for y in df_sorted_danceability.danceability.iloc[-10:].index], [3]])['name'])
artists = list((df.iloc[[int(y) for y in df_sorted_danceability.danceability.iloc[-10:].index], [9]])['artist'])
names = [x if "(feat." not in x else x[:x.index("(") - 1]for x in names]
py.ylabel("Danceability")
py.title("Songs with Lowest Danceability")
ax = py.gca()
del names[1]; names.insert(1, "Boulevard of Broken Dreams")
del names[4]; names.insert(3, "We Are The Champions")
del names[6]; names.insert(5, "Love Me Like Ypu Do")
py.axis(ymin=0.2, ymax=0.3)
py.xticks(x1, names, fontsize=5, rotation=23)
py.savefig('danceability_bar_bottom10')
