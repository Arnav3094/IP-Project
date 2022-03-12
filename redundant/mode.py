import create
from create import *

df = create.df
df_sorted_mode = df.sort_values(by=['mode'], ascending=True)

py.figure(dpi=300)
x = range(0, 2)
mode_counts = [list(df_sorted_mode['mode']).count(i) for i in x]
py.pie(mode_counts, labels=x, autopct='%1.0f%%')
py.legend(title='Mode Value:')
py.title("Distribution of Modes")
py.savefig('mode_pie')
py.close()
