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
py.xlabel("")
py.xticks(pd.Series(range(0, 21))/20, fontsize=7)
py.savefig('energy_hist')
py.close()
