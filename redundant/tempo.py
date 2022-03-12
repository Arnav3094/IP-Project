import create
from create import *

df = create.df
mean_df = create.mean_df
df_sorted_tempo = df.sort_values(by=['tempo'], ascending=False)
mean_df_sorted_tempo = mean_df.sort_values(by=['tempo'], ascending=False)

py.figure(dpi=450)
py.hist(df_sorted_tempo.tempo, bins=range(60, 220, 10), rwidth=0.7, color='#6EB972')
py.axis(xmin=60, xmax=210, ymax=150)
ax = py.gca()
py.xticks(range(60, 220, 10), fontsize=8)
py.yticks(range(0, 160, 10))
ax.yaxis.set_ticks_position('both')
ax.xaxis.set_ticks_position('both')
ax.yaxis.set_minor_locator(AutoMinorLocator())
py.grid()
py.title("Tempo Distribution")
py.xlabel("Tempo")
py.ylabel("Number of Tracks")
py.savefig('tempo_hist')
py.close()

x1 = range(5, 105, 10)
py.figure(dpi=450, figsize=(9, 6))
data = pd.Series(df_sorted_tempo.tempo.unique())
names = pd.Series(df_sorted_tempo.name.unique())
py.bar(x1, data.iloc[:10], width=5, color='#599BA7')
names = list(names.iloc[:10])
py.axis(ymin=185, ymax=210)
names_new = []
for name in names:
    words = name.split(" ")
    names_new.append([" ".join(words[i:i + 1]) for i in range(0, len(words), 1)])
for name in names_new:
    names_new[names_new.index(name)] = str.join("\n", name)
py.xticks(x1, names_new, fontsize=6.5)
py.title("Songs with the Highest Tempo")
py.ylabel("Tempo")
py.grid(axis='y')
ax = py.gca()
ax.yaxis.set_ticks_position('both')
ax.yaxis.set_minor_locator(AutoMinorLocator())
py.savefig('tempo_bar_top10')
py.close()

x1 = range(5, 105, 10)
py.figure(dpi=450, figsize=(9, 6))
data = pd.Series(df_sorted_tempo.tempo.unique())
names = pd.Series(df_sorted_tempo.name.unique())
py.bar(x1, data.iloc[-10:], width=5, color='#6BA708')
names = list(names.iloc[-10:])
py.axis(ymin=60, ymax=75)
names_new = []
for name in names:
    words = name.split(" ")
    names_new.append([" ".join(words[i:i + 1]) for i in range(0, len(words), 1)])
for name in names_new:
    names_new[names_new.index(name)] = str.join("\n", name)
py.xticks(x1, names_new, fontsize=6.5)
py.title("Songs with the Lowest Tempo")
py.ylabel("Tempo")
py.grid(axis='y')
ax = py.gca()
ax.yaxis.set_ticks_position('both')
ax.yaxis.set_minor_locator(AutoMinorLocator())
py.savefig('tempo_bar_bottom10')
py.close()
