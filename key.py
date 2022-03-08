import create
from create import *

df = create.df
df_sorted_key = df.sort_values(by=['key'], ascending=True)

py.figure(dpi=450)
x = range(-1, 12)
key_counts = [list(df_sorted_key.key).count(i) for i in x]
py.bar(x, key_counts)
py.plot(x, key_counts, linewidth=0.75, marker='.', color='#8F8F8F')
py.axis(xmax=12, xmin=-2)
ax = py.gca()
ax.yaxis.set_ticks_position('both')
py.grid(axis='y')
py.xticks(x)
py.title("Distribution of Keys")
py.xlabel("Key")
py.ylabel("Number of Tracks")
py.savefig('key_bar')
py.close()
