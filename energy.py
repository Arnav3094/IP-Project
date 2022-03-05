import create
from create import *

df = create.df
mean_df = create.mean_df
df_sorted_energy = df.sort_values(by=['energy'], ascending=False)
mean_df_sorted_energy = mean_df.sort_values(by=['energy'], ascending=False)

x = range(1, 1001)
py.figure(dpi=450)
py.hist(df_sorted_energy.energy, bins=pd.Series(range(0, 21))/20)
py.yticks(range(0, 130, 10))
ax = py.gca()
ax.yaxis.set_minor_locator(AutoMinorLocator())
py.grid()
py.axis(xmin=0, xmax=1)
py.title("Distribution of Energy")
py.xlabel("Energy")
py.ylabel("Number of Tracks")
py.xticks(pd.Series(range(0, 21))/20, fontsize=7)
py.savefig('energy_hist')
py.close()

x1 = range(5, 105, 10)
py.figure(dpi=450, figsize=(10, 5))
py.bar(x1, df_sorted_energy.energy.iloc[0:10], width=5)
py.axis(ymin=0.95, ymax=1)
names = list(df_sorted_energy.name.iloc[0:10])
# names_new = [re.sub("(.{10})", "\\1\n", label, 0, re.DOTALL) for label in names]
names_new = []
for name in names:
    words = name.split(" ")
    names_new.append([" ".join(words[i:i+2]) for i in range(0, len(words), 2)])
for name in names_new:
    names_new[names_new.index(name)] = str.join("\n", name)
py.xticks(x1, names_new, fontsize=6.5)
py.title("Most Energetic Songs")
py.ylabel("Energy")
py.savefig('energy_bar_top10')
