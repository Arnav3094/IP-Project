from create import *
import create

df = create.df
mean_df = create.mean_df

py.hist(df.popularity, bins=range(40, 98, 2), color='#FFBA71')
py.xticks(range(40, 100, 5))
py.title("Distribution of Popularity of Tracks")
py.grid()
py.axis(ymax=100)
py.ylabel("Number of Tracks")
py.xlabel("Popularity")
py.savefig('popularity_hist')
py.close()

py.hist(mean_df.popularity, bins=range(40, 100, 5))
py.title("Distribution of Average Popularity of Artists (by top 10 tracks)")
py.xticks(range(40, 100, 5))
py.axis(ymax=35)
py.ylabel("Number of artists")
py.xlabel("Popularity")
py.grid()
py.savefig('popularity_artists_hist')
py.close()

sorted_mean_df = mean_df.sort_values(by=['popularity'], ascending=False)
py.plot(sorted_mean_df.iloc[:10, 1], marker='.', color='orange', markersize=10)
py.title("Popularity of top 10 Artists (by top 10 tracks)")
py.xticks(fontsize=7, rotation=-20)
py.grid()
py.savefig('popularity_line_chart')
py.close()
