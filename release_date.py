from create import *
import create

df = create.df
mean_df = create.mean_df
df_album_release_date_sorted = df.sort_values(by=['album_release_date'])

py.figure(dpi=300)
py.hist(df_album_release_date_sorted.album_release_date.str.slice(0, 4).astype(int), bins=[x for x in range(1955, 2030, 5)], rwidth=0.9, color='#997BFF')
py.xticks(range(1955, 2030, 5), rotation=25)
py.ylabel('Number of Songs')
py.xlabel('Year of Release')
py.grid()
py.savefig('release_date_hist_year')
py.close()
