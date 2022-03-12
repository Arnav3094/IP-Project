from create import *
import create

df = create.df
mean_df = create.mean_df
df_sorted_popularity = df.sort_values(by=['popularity'], ascending=False)
mean_df_sorted_popularity = mean_df.sort_values(by=['popularity'], ascending=False)

py.figure(dpi=300)
py.hist(df.popularity, bins=range(40, 105, 5), color='#FFBA71')
py.xticks(range(40, 105, 5))
py.yticks(range(0, 275, 25))
py.title("Distribution of Popularity of Tracks")
py.grid()
py.ylabel("Number of Tracks")
py.xlabel("Popularity")
py.savefig('popularity_hist')
py.close()

py.figure(dpi=300)
py.hist(mean_df.popularity, bins=range(35, 100, 5))
py.title("Distribution of Popularity of Artists (by top 10 tracks)")
py.xticks(range(35, 100, 5))
py.axis(ymax=35)
py.ylabel("Number of artists")
py.xlabel("Popularity")
py.grid()
py.savefig('popularity_artists_hist')
py.close()

py.figure(dpi=300)
py.plot(mean_df_sorted_popularity.iloc[:10, 1], marker='.', color='orange', markersize=10)
py.title("Popularity of top 10 Artists (by top 10 tracks)")
py.xticks(fontsize=7, rotation=-20)
py.yticks(range(84, 92))
py.grid()
py.savefig('popularity_line_artists_top10')
py.close()

x1 = range(5, 105, 10)
py.figure(dpi=450, figsize=(7, 5))
py.bar(x1, df_sorted_popularity.popularity.iloc[0:10], width=5, color='#CB522E')
names = list(df_sorted_popularity.name.iloc[0:10])
py.axis(ymin=90, ymax=98)
names_new = []
for name in names:
    words = name.split(" ")
    names_new.append([" ".join(words[i:i + 1]) for i in range(0, len(words), 1)])
for name in names_new:
    names_new[names_new.index(name)] = str.join("\n", name)
py.xticks(x1, names_new, fontsize=6)
py.title("Most Popular Songs")
py.ylabel("Popularity (out of 100)")
py.grid(axis='y')
ax = py.gca()
ax.yaxis.set_ticks_position('both')
py.savefig('popularity_bar_top10')
py.close()
