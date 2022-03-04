from create import *
import create

df = create.df
mean_df = create.mean_df
mean_df_sorted_duration = mean_df.sort_values(by=['duration_sec'], ascending=False)
df_sorted_duration = df.sort_values(by=['duration_sec'], ascending=False)

py.figure(dpi=300)
py.xticks(range(60, 660, 30), fontsize=8)
py.yticks(range(0, 325, 25))
py.hist(df_sorted_duration.duration_sec, bins=range(60, 660, 30), rwidth=0.8, color='#FF8A82')
py.axis(xmin=50, xmax=640)
ax = py.gca()
ax.yaxis.set_minor_locator(AutoMinorLocator())
py.xlabel("Duration in Seconds")
py.ylabel("No. of Songs")
py.title("Distribution of duration")
py.grid(which='major', color='#777777')
py.grid(which='minor', color='#ACACAC', linestyle='dotted')
py.savefig('duration')
py.close()


x = range(5, 55, 5)
py.figure(dpi=300)
py.bar(x, height=mean_df_sorted_duration.duration_sec.iloc[0:10], width=2, color="#3CBCFF")
py.plot(x, mean_df_sorted_duration.duration_sec.iloc[0:10], color='#3CBCFF', marker=".", markersize=10)
py.axis(ymin=260)
ax = py.gca()
ax.yaxis.set_minor_locator(AutoMinorLocator())
py.grid()
py.title("Top 10 highest Average duration for top 10 tracks")
py.ylabel("Duration")
ticks = [x if x != "The Notorious B.I.G." else "Biggie" for x in mean_df_sorted_duration.duration_sec.iloc[0:10].index]
py.xticks(x, ticks, fontsize=6, rotation=-15)
py.savefig('duration_bar_avg')
