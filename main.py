import create
from create import *
from difflib import get_close_matches
from PIL import Image as img
import danceability

df = create.df
mean_df = create.mean_df
main_menu = """Main Menu:
1. DataFrame              2. Search for Artists in DataFrame 
3. Graph for Mode         4. Graph for Release Date 
5. Graph for Key          6. Popularity Menu
7. Duration Menu          8. Danceability Menu
9. Energy Menu            10. Loudness Menu
11. Valence Menu          12. Speechiness Menu
13. Acousticness Menu     14. Instrumentalness Menu
15. Liveness Menu         16. Tempo Menu
To exit any menu press 'q' or 'Q'"""
popularity_menu = "\nPopularity Menu:\n1. Show Track Popularity Distribution\t\t2. Show Artist Popularity Distribution\n3. Show Artists with Highest Popularity\t\t4. Show Songs with Highest Popularity\n>>>"
duration_menu = "\nDuration Menu:\n1. Show Duration Distribution Histogram\t\t2. Show Artists with Highest Average Duration\n>>>"
loudness_menu = "\nLoudness Menu:\n1. Show Loudness Distribution Histogram\t\t2. Show Loudest Songs\n3. Show Loudest Artists\n>>>"
tempo_menu = "\nTempo Menu:\n1. Show Tempo Distribution Histogram\t\t2. Show Fastest Songs\n3. Show Slowest Songs\n>>>"


def menu(dpnt: str):
    return f"\n{dpnt} Menu:\n1. Show {dpnt} Distribution Histogram\t\t2. Show Songs with the Highest {dpnt}\n3. Show Artists with the Highest {dpnt}\n>>>"


def show_df():
    pp(df.loc[:, 'name':])


def show_artist():
    inp_ = 0
    while inp_ not in ['q', 'Q']:
        artists_ = df.artist.unique()
        inp_ = input("Enter Artist Name or press 'i' to list of Artists: ")
        if inp_ in ['q', 'Q']:
            break
        if inp_ in ['i', 'I']:
            pp(", ".join(create.artists))
            inp_ = input("Enter Artist Name: ")
        if inp_ in artists_:
            pp(df[df['artist'] == inp_.lower()].loc[:, 'name':])
        else:
            close_matches = get_close_matches(inp_, artists_, 3, 0.1)
            if len(close_matches):
                inp__ = input(f"Did you mean any of {close_matches}?\n(Enter no or 1, 2, or 3 to select)\n>>>")
                try:
                    inp_ = close_matches[int(inp__)-1]
                    pp(df[df['artist'] == inp_].loc[:, 'name':])
                except ValueError or IndexError:
                    print("Artist data unavailable")
                except Exception as e_:
                    print(e_)
            else:
                print("Artist data unavailable")


def show_mode():
    df_sorted_mode = df.sort_values(by=['mode'], ascending=True)
    py.figure(dpi=300)
    x = range(0, 2)
    mode_counts = [list(df_sorted_mode['mode']).count(i) for i in x]
    py.pie(mode_counts, labels=x, autopct='%1.0f%%')
    py.legend(title='Mode Value:')
    py.title("Distribution of Modes")
    py.savefig('mode_pie')
    py.close()
    print("Graph saved in enclosing folder and opened in new window")
    img.open('mode_pie.png').show()


def show_release_date():
    df_album_release_date_sorted = df.sort_values(by=['album_release_date'])
    py.figure(dpi=300)
    py.hist(df_album_release_date_sorted.album_release_date.str.slice(0, 4).astype(int),
            bins=[x for x in range(1955, 2030, 5)], rwidth=0.9, color='#997BFF')
    py.xticks(range(1955, 2030, 5), rotation=25)
    py.ylabel('Number of Songs')
    py.xlabel('Year of Release')
    py.grid()
    py.savefig('release_date_hist_year')
    py.close()
    print("Graph saved in enclosing folder and opened in new window")
    img.open('release_date_hist_year.png').show()


def show_key():
    df_sorted_key = df.sort_values(by=['key'], ascending=True)
    py.figure(dpi=450)
    x = range(-1, 12)
    key_counts = [list(df_sorted_key.key).count(i) for i in x]
    py.bar(x, key_counts, color='#8F4A45')
    py.plot(x, key_counts, linewidth=0.75, marker='.', color='#8F8F8F')
    py.axis(xmax=11.5, xmin=-1.5)
    ax = py.gca()
    ax.yaxis.set_ticks_position('both')
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    py.grid(axis='y')
    py.xticks(x)
    py.title("Distribution of Keys")
    py.xlabel("Key")
    py.ylabel("Number of Tracks")
    py.savefig('key_bar')
    py.close()
    print("Graph saved in enclosing folder and opened in new window")
    img.open('key_bar.png').show()


def show_duration():
    inp_ = 0
    df_sorted_duration = df.sort_values(by=['duration_sec'], ascending=False)
    mean_df_sorted_duration = mean_df.sort_values(by=['duration_sec'], ascending=False)
    while inp_ not in ['Q', 'q']:
        inp_ = input(duration_menu)
        if inp_ in ['Q', 'q']: break
        if inp_ == '1':
            py.figure(dpi=300)
            py.xticks(range(60, 660, 30), fontsize=8)
            py.yticks(range(0, 325, 25))
            py.hist(df_sorted_duration.duration_sec, bins=range(60, 660, 30), rwidth=0.8, color='#FF8A82')
            py.axis(xmin=50, xmax=640, ymax=300)
            py.gca().yaxis.set_minor_locator(AutoMinorLocator())
            py.xlabel("Duration in Seconds")
            py.ylabel("No. of Songs")
            py.title("Distribution of Duration")
            py.grid(which='major', color='#777777')
            py.grid(which='minor', color='#ACACAC', linestyle='dashed', linewidth=0.3)
            py.savefig('duration_hist')
            py.close()
            print("Graph saved in enclosing folder and opened in new window")
            img.open('duration_hist.png').show()
        if inp_ == '2':
            x = range(5, 55, 5)
            py.figure(dpi=300)
            py.bar(x, height=mean_df_sorted_duration.duration_sec.iloc[0:10], width=2, color="#3CBCFF")
            py.plot(x, mean_df_sorted_duration.duration_sec.iloc[0:10], color='#3CBCFF', marker=".", markersize=10)
            py.axis(ymin=260, ymax=320)
            ax = py.gca()
            ax.yaxis.set_minor_locator(AutoMinorLocator())
            py.grid()
            py.title("Artists with Highest Average Duration")
            py.ylabel("Duration (in s)")
            ticks = [x if x != "The Notorious B.I.G." else "Biggie" for x in
                     mean_df_sorted_duration.duration_sec.iloc[0:10].index]
            py.xticks(x, ticks, fontsize=6, rotation=-15)
            py.savefig('duration_bar_artists_top10')
            print("Graph saved in enclosing folder and opened in new window")
            img.open('duration_bar_artists_top10.png').show()
        else:
            print("Invalid Input")


def show_tempo():
    inp_ = 0
    df_sorted_tempo = df.sort_values(by=['tempo'], ascending=False)
    while inp_ not in ['Q', 'q']:
        inp_ = input(tempo_menu)
        if inp_ in ['Q', 'q']: break
        if inp_ == '1':
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
            print("Graph saved in enclosing folder and opened in new window")
            img.open('tempo_hist.png').show()
        elif inp_ == '2':
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
            for name in names_new: names_new[names_new.index(name)] = str.join("\n", name)
            py.xticks(x1, names_new, fontsize=6.5)
            py.title("Songs with the Highest Tempo")
            py.ylabel("Tempo")
            py.grid(axis='y')
            ax = py.gca()
            ax.yaxis.set_ticks_position('both')
            ax.yaxis.set_minor_locator(AutoMinorLocator())
            py.savefig('tempo_bar_top10')
            py.close()
            print("Graph saved in enclosing folder and opened in new window")
            img.open('tempo_bar_top10.png').show()
        elif inp_ == '3':
            py.figure(dpi=450, figsize=(9, 6))
            data = pd.Series(df_sorted_tempo.tempo.unique())
            names = pd.Series(df_sorted_tempo.name.unique())
            py.bar(x1, data.iloc[-10:][::-1], width=5, color='#6BA708')
            names = list(names.iloc[-10:])[::-1]
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
            print("Graph saved in enclosing folder and opened in new window")
            img.open('tempo_bar_bottom10.png').show()
        else:
            print("Invalid Input")


def show_danceability():
    inp_ = 0
    while inp_ not in ['Q', 'q']:
        inp_ = input(menu("Danceability"))
        if inp_ in ['Q', 'q']: break
        elif inp_ == '1':
            danceability.danceability_hist()
            print("Graph saved in enclosing folder and opened in new window")
            img.open('danceability_hist.png').show()
        elif inp_ == '2':
            danceability.danceability_bar_top10()
            print("Graph saved in enclosing folder and opened in new window")
            img.open('danceability_bar_top10.png').show()
        elif inp_ == '3':
            danceability.danceability_bar_artists_top10()
            print("Graph saved in enclosing folder and opened in new window")
            img.open('danceability_bar_artists_top10.png').show()
        else:
            print("Invalid Input")


def show_energy():
    inp_ = 0
    df_sorted_energy = df.sort_values(by=['energy'], ascending=False)
    mean_df_sorted_energy = mean_df.sort_values(by=['energy'], ascending=False)
    while inp_ not in ['Q', 'q']:
        inp_ = input(menu("Energy"))
        if inp_ in ['Q', 'q']: break
        elif inp_ == '1':
            py.figure(dpi=450)
            py.hist(df_sorted_energy.energy, bins=pd.Series(range(0, 21))/20)
            py.yticks(range(0, 130, 10))
            ax = py.gca()
            ax.yaxis.set_minor_locator(AutoMinorLocator())
            py.grid()
            py.axis(xmin=0, xmax=1, ymax=120)
            py.title("Distribution of Energy")
            py.xlabel("Energy")
            py.ylabel("Number of Tracks")
            py.xticks(pd.Series(range(0, 21))/20, fontsize=7)
            py.savefig('energy_hist')
            py.close()
            print("Graph saved in enclosing folder and opened in new window")
            img.open('energy_hist.png').show()
        elif inp_ == '2':
            py.figure(dpi=450, figsize=(10, 5))
            py.bar(x1, df_sorted_energy.energy.iloc[0:10], width=5, color='#FFE695')
            py.axis(ymin=0.95, ymax=1)
            names = list(df_sorted_energy.name.iloc[0:10])
            names_new = []
            for name in names:
                words = name.split(" ")
                names_new.append([" ".join(words[i:i+2]) for i in range(0, len(words), 2)])
            for name in names_new:
                names_new[names_new.index(name)] = str.join("\n", name)
            py.xticks(x1, names_new, fontsize=6.5)
            py.title("Most Energetic Songs")
            py.ylabel("Energy")
            py.grid(axis='y')
            py.savefig('energy_bar_top10')
            py.close()
            print("Graph saved in enclosing folder and opened in new window")
            img.open('energy_bar_top10.png').show()
        elif inp_ == '3':
            py.figure(dpi=450, figsize=(7, 4))
            py.bar(x1, mean_df_sorted_energy.energy.iloc[0:10], width=5, color='#FF005D')
            artists_ = mean_df_sorted_energy.iloc[0:10, 1:2].index
            artists_new = []
            for artist in artists_:
                words = artist.split(" ")
                artists_new.append([" ".join(words[i:i + 1]) for i in range(0, len(words), 1)])
            for artist in artists_new:
                artists_new[artists_new.index(artist)] = str.join("\n", artist)
            py.xticks(x1, artists_new, fontsize=7)
            py.title("Most Energetic Artists")
            py.ylabel("Energy")
            py.axis(ymin=0.75, ymax=0.9)
            py.grid(axis='y')
            py.gca().yaxis.set_minor_locator(AutoMinorLocator())
            py.gca().yaxis.set_ticks_position('both')
            py.savefig('energy_bar_artists_top10')
            print("Graph saved in enclosing folder and opened in new window")
            img.open('energy_bar_artists_top10.png').show()
        else:
            print("Invalid Input")


def show_loudness():
    inp_ = 0
    df_sorted_loudness = df.sort_values(by=['loudness'], ascending=False)
    mean_df_sorted_loudness = mean_df.sort_values(by=['loudness'], ascending=False)
    while inp_ not in ['Q', 'q']:
        inp_ = input(loudness_menu)
        if inp_ in ['Q', 'q']: break
        elif inp_ == '1':
            py.figure(dpi=450)
            py.hist(df_sorted_loudness.loudness, bins=range(-23, 0, 1), rwidth=0.7, color='#51A063')
            py.axis(xmax=0, xmin=-23)
            ax = py.gca()
            ax.yaxis.tick_right()
            ax.yaxis.set_ticks_position('both')
            ax.yaxis.set_minor_locator(AutoMinorLocator())
            ax.xaxis.set_minor_locator(AutoMinorLocator())
            py.grid()
            py.title("Distribution of Loudness")
            py.xlabel("Loudness")
            py.ylabel("Number of Tracks")
            py.savefig('loudness_hist')
            py.close()
            print("Graph saved in enclosing folder and opened in new window")
            img.open('loudness_hist.png').show()
        elif inp_ == '2':
            py.figure(dpi=450, figsize=(9, 5))
            py.bar(x1, df_sorted_loudness.loudness.iloc[0:10], width=5, )
            names = list(df_sorted_loudness.name.iloc[0:10])
            py.yticks(np.array(range(-10, 1)) / 4)
            py.axis(ymax=0, ymin=-2.5)
            names_new = []
            for name in names:
                words = name.split(" ")
                names_new.append([" ".join(words[i:i + 2]) for i in range(0, len(words), 2)])
            for name in names_new:
                names_new[names_new.index(name)] = str.join("\n", name)
            py.xticks(x1, names_new, fontsize=6.5)
            py.title("Loudest Songs")
            py.ylabel("Loudness")
            py.grid(axis='y')
            py.savefig('loudness_bar_top10')
            py.close()
            print("Graph saved in enclosing folder and opened in new window")
            img.open('loudness_bar_top10.png').show()
        elif inp_ == '3':
            py.figure(dpi=450, figsize=(8, 5))
            py.bar(x1, mean_df_sorted_loudness.loudness.iloc[0:10], width=5, color='#FF005D')
            artists_ = mean_df_sorted_loudness.iloc[0:10, 1:2].index
            py.xticks(x1, artists_, fontsize=6.5)
            py.title("Loudest Artists")
            py.ylabel("Loudness")
            py.yticks(np.array(range(-20, -13)) / 4)
            py.grid(axis='y')
            py.axis(ymin=-4.75, ymax=-3.5)
            ax = py.gca()
            ax.yaxis.set_minor_locator(AutoMinorLocator())
            ax.yaxis.set_ticks_position('both')
            py.savefig('loudness_bar_artists_top10')
            py.close()
            print("Graph saved in enclosing folder and opened in new window")
            img.open('loudness_bar_artists_top10.png').show()
        else:
            print("Invalid Input")


def show_valence():
    inp_ = 0
    df_sorted_valence = df.sort_values(by=['valence'], ascending=False)
    mean_df_sorted_valence = mean_df.sort_values(by=['valence'], ascending=False)
    df_sorted_valence.valence *= 100
    mean_df_sorted_valence *= 100
    while inp_ not in ['Q', 'q']:
        inp_ = input(menu("Valence"))
        if inp_ in ['Q', 'q']: break
        elif inp_ == '1':
            py.figure(dpi=450)
            py.hist(df_sorted_valence.valence, bins=range(0, 105, 5), rwidth=0.7, color='#C86A72')
            py.axis(xmin=-1, xmax=101, ymax=90)
            ax = py.gca()
            py.xticks(range(0, 105, 5), fontsize=8)
            ax.yaxis.set_ticks_position('both')
            ax.yaxis.set_minor_locator(AutoMinorLocator())
            py.grid()
            py.title("Distribution of Valence")
            py.xlabel("Valence (out of 100)")
            py.ylabel("Number of Tracks")
            py.savefig('valence_hist')
            py.close()
            print("Graph saved in enclosing folder and opened in new window")
            img.open('valence_hist.png').show()
        elif inp_ == '2':
            py.figure(dpi=450)
            py.bar(x1, df_sorted_valence.valence.iloc[0:10], width=5, color='#C80045')
            names = list(df_sorted_valence.name.iloc[0:10])
            py.axis(ymin=96, ymax=97.5)
            py.yticks([96, 96.25, 96.5, 96.75, 97, 97.25, 97.5])
            names_new = []
            for name in names:
                words = name.split(" ")
                names_new.append([" ".join(words[i:i + 1]) for i in range(0, len(words), 1)])
            for name in names_new:
                names_new[names_new.index(name)] = str.join("\n", name)
            py.xticks(x1, names_new, fontsize=6)
            py.title("Songs with the Highest Valence")
            py.ylabel("Valence (out of 100)")
            py.grid(axis='y')
            ax = py.gca()
            ax.yaxis.set_ticks_position('both')
            ax.yaxis.set_minor_locator(AutoMinorLocator())
            py.savefig('valence_bar_top10')
            py.close()
            print("Graph saved in enclosing folder and opened in new window")
            img.open('valence_bar_top10.png').show()
        elif inp_ == '3':
            py.figure(dpi=450)
            py.bar(x1, mean_df_sorted_valence.valence.iloc[0:10], width=5, color='#00A995')
            artists_ = list(mean_df_sorted_valence.iloc[0:10, 1:2].index)
            try: artists_[artists_.index("Joey Bada$$")] = "Joey Badass"
            except ValueError: pass
            except Exception as e: print(e)
            artists_new = []
            for artist in artists_:
                words = artist.split(" ")
                artists_new.append([" ".join(words[i:i + 1]) for i in range(0, len(words), 1)])
            for artist in artists_new: artists_new[artists_new.index(artist)] = str.join("\n", artist)
            py.xticks(x1, artists_new, fontsize=7)
            py.title("Artists with the Highest Valence")
            py.ylabel("Valence (out of 100)")
            py.axis(ymin=65, ymax=77)
            py.yticks(range(65, 78))
            py.grid(axis='y', which='major')
            ax = py.gca()
            ax.yaxis.set_minor_locator(AutoMinorLocator())
            ax.yaxis.set_ticks_position('both')
            py.savefig('valence_bar_artists_top10')
            py.close()
            print("Graph saved in enclosing folder and opened in new window")
            img.open('valence_bar_artists_top10.png').show()
        else:
            print("Invalid Input")


def show_speechiness():
    inp_ = 0
    df_sorted_speechiness = df.sort_values(by=['speechiness'], ascending=False)
    mean_df_sorted_speechiness = mean_df.sort_values(by=['speechiness'], ascending=False)
    df_sorted_speechiness.speechiness *= 100
    mean_df_sorted_speechiness *= 100
    while inp_ not in ['Q', 'q']:
        inp_ = input(menu("Speechiness"))
        if inp_ in ['Q', 'q']: break
        elif inp_ == '1':
            py.figure(dpi=450)
            py.hist(df_sorted_speechiness.speechiness, bins=range(0, 56, 2), rwidth=0.7, color='#51A063')
            py.axis(xmin=0, xmax=55, ymax=275)
            ax = py.gca()
            py.xticks(range(0, 56, 2), fontsize=8)
            py.yticks(range(0, 300, 25))
            ax.yaxis.set_ticks_position('both')
            ax.yaxis.set_minor_locator(AutoMinorLocator())
            py.grid()
            py.title("Distribution of Speechiness")
            py.xlabel("Speechiness (out of 100)")
            py.ylabel("Number of Tracks")
            py.savefig('speechiness_hist')
            py.close()
            print("Graph saved in enclosing folder and opened in new window")
            img.open('speechiness_hist.png').show()
        elif inp_ == '2':
            py.figure(dpi=450, figsize=(7, 5))
            py.bar(x1, df_sorted_speechiness.speechiness.iloc[0:10], width=5, color='#5928A9')
            names = list(df_sorted_speechiness.name.iloc[0:10])
            py.axis(ymin=40, ymax=55)
            py.yticks(range(40, 56))
            names_new = []
            for name in names:
                words = name.split(" ")
                names_new.append([" ".join(words[i:i + 2]) for i in range(0, len(words), 2)])
            for name in names_new:
                names_new[names_new.index(name)] = str.join("\n", name)
            py.xticks(x1, names_new, fontsize=6)
            py.title("Songs with the Highest Speechiness")
            py.ylabel("Speechiness (out of 100)")
            py.grid(axis='y')
            ax = py.gca()
            ax.yaxis.set_ticks_position('both')
            ax.yaxis.set_minor_locator(AutoMinorLocator())
            py.savefig('speechiness_bar_top10')
            py.close()
            print("Graph saved in enclosing folder and opened in new window")
            img.open('speechiness_bar_top10.png').show()
        elif inp_ == '3':
            py.figure(dpi=450)
            py.bar(x1, mean_df_sorted_speechiness.speechiness.iloc[0:10], width=5, color='#00A995')
            artists_ = list(mean_df_sorted_speechiness.iloc[0:10, 1:2].index)
            try: artists_[artists_.index("Joey Bada$$")] = "Joey Badass"
            except ValueError: pass
            except Exception as e: print(e)
            artists_new = []
            for artist in artists_:
                words = artist.split(" ")
                artists_new.append([" ".join(words[i:i + 1]) for i in range(0, len(words), 1)])
            for artist in artists_new: artists_new[artists_new.index(artist)] = str.join("\n", artist)
            py.xticks(x1, artists_new, fontsize=7)
            py.yticks(range(20, 33))
            py.title("Artists with the Highest Speechiness")
            py.ylabel("Speechiness (out of 100)")
            py.axis(ymin=20, ymax=32)
            py.grid(axis='y')
            ax = py.gca()
            ax.yaxis.set_minor_locator(AutoMinorLocator())
            ax.yaxis.set_ticks_position('both')
            py.savefig('speechiness_bar_artists_top10')
            py.close()
            print("Graph saved in enclosing folder and opened in new window")
            img.open('speechiness_bar_artists_top10.png').show()
        else:
            print("Invalid Input")


def show_acousticness():
    inp_ = 0
    df_sorted_acousticness = df.sort_values(by=['acousticness'], ascending=False)
    mean_df_sorted_acousticness = mean_df.sort_values(by=['acousticness'], ascending=False)
    df_sorted_acousticness.acousticness *= 100
    mean_df_sorted_acousticness *= 100
    while inp_ not in ['Q', 'q']:
        inp_ = input(menu("Acousticness"))
        if inp_ in ['Q', 'q']: break
        elif inp_ == '1':
            py.figure(dpi=450)
            py.hist(df_sorted_acousticness.acousticness, bins=range(0, 105, 5), rwidth=0.7, color='#A90036')
            py.axis(xmin=-1, xmax=101, ymax=300)
            ax = py.gca()
            py.xticks(range(0, 105, 5), fontsize=8)
            py.yticks(range(0, 325, 25))
            ax.yaxis.set_ticks_position('both')
            ax.xaxis.set_ticks_position('both')
            ax.yaxis.set_minor_locator(AutoMinorLocator())
            py.grid()
            py.title("Distribution of Acousticness")
            py.xlabel("Acousticness (out of 100)")
            py.ylabel("Number of Tracks")
            py.savefig('acousticness_hist')
            py.close()
            print("Graph saved in enclosing folder and opened in new window")
            img.open('acousticness_hist.png').show()
        elif inp_ == '2':
            py.figure(dpi=450, figsize=(7, 5))
            py.bar(x1, df_sorted_acousticness.acousticness.iloc[0:10], width=5, color='#CB522E')
            names = list(df_sorted_acousticness.name.iloc[0:10])
            py.axis(ymin=95, ymax=98)
            py.yticks(np.array(range(190, 197))/2)
            names_new = []
            for name in names:
                words = name.split(" ")
                names_new.append([" ".join(words[i:i + 2]) for i in range(0, len(words), 2)])
            for name in names_new:
                names_new[names_new.index(name)] = str.join("\n", name)
            py.xticks(x1, names_new, fontsize=6)
            py.title("Songs with the Highest Acousticness")
            py.ylabel("Acousticness (out of 100)")
            py.grid(axis='y')
            ax = py.gca()
            ax.yaxis.set_ticks_position('both')
            ax.yaxis.set_minor_locator(AutoMinorLocator())
            py.savefig('acousticness_bar_top10')
            py.close()
            print("Graph saved in enclosing folder and opened in new window")
            img.open('acousticness_bar_top10.png').show()
        elif inp_ == '3':
            py.figure(dpi=450)
            py.bar(x1, mean_df_sorted_acousticness.acousticness.iloc[0:10], width=5, color='#00A995')
            artists = list(mean_df_sorted_acousticness.iloc[0:10, 1:2].index)
            try: artists[artists.index("Joey Bada$$")] = "Joey Badass"
            except ValueError:
                pass
            except Exception as e:
                print(e)
            artists_new = []
            for artist in artists:
                words = artist.split(" ")
                artists_new.append([" ".join(words[i:i + 1]) for i in range(0, len(words), 1)])
            for artist in artists_new:
                artists_new[artists_new.index(artist)] = str.join("\n", artist)
            py.xticks(x1, artists_new, fontsize=7)
            py.title("Artists with the Highest Acousticness")
            py.ylabel("Acousticness (out of 100)")
            py.axis(ymin=50, ymax=95)
            py.grid(axis='y')
            ax = py.gca()
            ax.yaxis.set_minor_locator(AutoMinorLocator())
            ax.yaxis.set_ticks_position('both')
            py.savefig('acousticness_bar_artists_top10')
            py.close()
            print("Graph saved in enclosing folder and opened in new window")
            img.open('acousticness_bar_artists_top10.png').show()
        else:
            print("Invalid Input")


def show_instrumentalness():
    inp_ = 0
    df_sorted_instrumentalness = df.sort_values(by=['instrumentalness'], ascending=False)
    mean_df_sorted_instrumentalness = mean_df.sort_values(by=['instrumentalness'], ascending=False)
    df_sorted_instrumentalness.instrumentalness *= 100
    mean_df_sorted_instrumentalness *= 100
    while inp_ not in ['Q', 'q']:
        inp_ = input(menu("Instrumentalness"))
        if inp_ in ['Q', 'q']: break
        elif inp_ == '1':
            py.figure(dpi=450, figsize=(6, 7))
            py.hist(df_sorted_instrumentalness.instrumentalness, bins=range(0, 105, 5), rwidth=0.7, color='#A90036')
            py.axis(xmin=-1, xmax=101)
            ax = py.gca()
            py.yscale('log')
            ax.yaxis.set_ticks_position('both')
            ax.xaxis.set_ticks_position('both')
            py.grid()
            py.title("(Logarithmic) Distribution of Instrumentalness")
            py.xlabel("Instrumentalness")
            py.ylabel("Number of Tracks")
            py.savefig('instrumentalness_log_hist')
            py.close()
            print("Graph saved in enclosing folder and opened in new window")
            img.open('instrumentalness_log_hist.png').show()
        elif inp_ == '2':
            py.figure(dpi=450, figsize=(7, 5))
            py.bar(x1, df_sorted_instrumentalness.instrumentalness.iloc[0:10], width=5, color='#C4C82F')
            names = list(df_sorted_instrumentalness.name.iloc[0:10])
            py.axis(ymin=80, ymax=95)
            py.yticks(range(80, 96))
            names_new = []
            for name in names:
                words = name.split(" ")
                names_new.append([" ".join(words[i:i + 2]) for i in range(0, len(words), 2)])
            for name in names_new:
                names_new[names_new.index(name)] = str.join("\n", name)
            py.xticks(x1, names_new, fontsize=6)
            py.title("Songs with the Highest Instrumentalness")
            py.ylabel("Instrumentalness (out of 100)")
            py.grid(axis='y')
            ax = py.gca()
            ax.yaxis.set_ticks_position('both')
            ax.yaxis.set_minor_locator(AutoMinorLocator())
            py.savefig('instrumentalness_bar_top10')
            py.close()
            print("Graph saved in enclosing folder and opened in new window")
            img.open('instrumentalness_bar_top10.png').show()
        elif inp_ == '3':
            py.figure(dpi=450)
            py.bar(x1, mean_df_sorted_instrumentalness.instrumentalness.iloc[0:10], width=5, color='#75C883')
            artists = list(mean_df_sorted_instrumentalness.iloc[0:10, 1:2].index)
            py.yscale('log')
            try: artists[artists.index("Joey Bada$$")] = "Joey Badass"
            except ValueError: pass
            except Exception as e: print(e)
            artists_new = []
            for artist in artists:
                words = artist.split(" ")
                artists_new.append([" ".join(words[i:i + 1]) for i in range(0, len(words), 1)])
            for artist in artists_new: artists_new[artists_new.index(artist)] = str.join("\n", artist)
            py.xticks(x1, artists_new, fontsize=7)
            py.title("Artists with the Highest Instrumentalness (Logarithmic)")
            py.ylabel("Instrumentalness (out of 100)")
            py.axis(ymin=5, ymax=81)
            py.grid(axis='y', which='major')
            py.grid(axis='y', which='minor', linewidth=0.3)
            ax = py.gca()
            ax.yaxis.set_minor_formatter(ScalarFormatter())
            ax.yaxis.set_major_formatter(ScalarFormatter())
            ax.yaxis.set_ticks_position('both')
            py.savefig('instrumentalness_log_bar_artists_top10')
            py.close()
            print("Graph saved in enclosing folder and opened in new window")
            img.open('instrumentalness_log_bar_artists_top10.png').show()
        else:
            print("Invalid Input")


def show_liveness():
    inp_ = 0
    df_sorted_liveness = df.sort_values(by=['liveness'], ascending=False)
    mean_df_sorted_liveness = mean_df.sort_values(by=['liveness'], ascending=False)
    df_sorted_liveness.liveness *= 100
    mean_df_sorted_liveness *= 100
    while inp_ not in ['Q', 'q']:
        inp_ = input(menu("Liveness"))
        if inp_ in ['Q', 'q']: break
        elif inp_ == '1':
            py.figure(dpi=450)
            py.hist(df_sorted_liveness.liveness, bins=range(0, 105, 5), rwidth=0.7, color='#C86A72')
            py.axis(xmin=-1, xmax=101, ymax=325)
            ax = py.gca()
            py.xticks(range(0, 105, 5), fontsize=8)
            py.yticks(range(0, 350, 25))
            ax.yaxis.set_ticks_position('both')
            ax.xaxis.set_ticks_position('both')
            ax.yaxis.set_minor_locator(AutoMinorLocator())
            py.grid()
            py.title("Distribution of Liveness")
            py.xlabel("Liveness (out of 100)")
            py.ylabel("Number of Tracks")
            py.savefig('liveness_hist')
            py.close()
            print("Graph saved in enclosing folder and opened in new window")
            img.open('liveness_hist.png').show()
        elif inp_ == '2':
            py.figure(dpi=450)
            py.bar(x1, df_sorted_liveness.liveness.iloc[0:10], width=5, color='#CB522E')
            names = list(df_sorted_liveness.name.iloc[0:10])
            py.axis(ymin=75, ymax=95)
            names_new = []
            for name in names:
                words = name.split(" ")
                names_new.append([" ".join(words[i:i + 1]) for i in range(0, len(words), 1)])
            for name in names_new:
                names_new[names_new.index(name)] = str.join("\n", name)
            py.xticks(x1, names_new, fontsize=6)
            py.title("Songs with the Highest Liveness")
            py.ylabel("Liveness (out of 100)")
            py.grid(axis='y')
            ax = py.gca()
            ax.yaxis.set_ticks_position('both')
            ax.yaxis.set_minor_locator(AutoMinorLocator())
            py.savefig('liveness_bar_top10')
            py.close()
            print("Graph saved in enclosing folder and opened in new window")
            img.open('liveness_bar_top10.png').show()
        elif inp_ == '3':
            py.figure(dpi=450)
            py.bar(x1, mean_df_sorted_liveness.liveness.iloc[0:10], width=5, color='#00A995')
            artists_ = list(mean_df_sorted_liveness.iloc[0:10, 1:2].index)
            try: artists_[artists_.index("Joey Bada$$")] = "Joey Badass"
            except ValueError: pass
            except Exception as e: print(e)
            artists_new = []
            for artist in artists_:
                words = artist.split(" ")
                artists_new.append([" ".join(words[i:i + 1]) for i in range(0, len(words), 1)])
            for artist in artists_new: artists_new[artists_new.index(artist)] = str.join("\n", artist)
            py.xticks(x1, artists_new, fontsize=7)
            py.title("Artists with the Highest Liveness")
            py.ylabel("Liveness (out of 100)")
            py.axis(ymin=27, ymax=37.5)
            py.yticks(np.array(range(55, 76, 5))/2)
            py.grid(axis='y', which='major')
            py.grid(axis='y', which='minor', linewidth=0.3)
            ax = py.gca()
            ax.yaxis.set_minor_locator(AutoMinorLocator())
            ax.yaxis.set_ticks_position('both')
            ax.yaxis.set_minor_formatter(ScalarFormatter())
            ax.tick_params(which='minor', axis='y', labelsize=7)
            py.savefig('liveness_bar_artists_top10')
            py.close()
            print("Graph saved in enclosing folder and opened in new window")
            img.open('liveness_bar_artists_top10.png').show()
        else:
            print("Invalid Input")


def show_popularity():
    inp_ = 0
    df_sorted_popularity = df.sort_values(by=['popularity'], ascending=False)
    mean_df_sorted_popularity = mean_df.sort_values(by=['popularity'], ascending=False)
    while inp_ not in ['Q', 'q']:
        inp_ = input(popularity_menu)
        if inp_ in ['Q', 'q']: break
        elif inp_ == '1':
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
            print("Graph saved in enclosing folder and opened in new window")
            img.open('popularity_hist.png').show()
        elif inp_ == '2':
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
            print("Graph saved in enclosing folder and opened in new window")
            img.open('popularity_artists_hist.png').show()
        elif inp_ == '3':
            py.figure(dpi=300)
            py.plot(mean_df_sorted_popularity.iloc[:10, 1], marker='.', color='orange', markersize=10)
            py.title("Popularity of top 10 Artists (by top 10 tracks)")
            py.xticks(fontsize=7, rotation=-20)
            py.yticks(range(84, 92))
            py.grid()
            py.savefig('popularity_line_artists_top10')
            py.close()
            print("Graph saved in enclosing folder and opened in new window")
            img.open('popularity_line_artists_top10.png').show()
        elif inp_ == '4':
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
            print("Graph saved in enclosing folder and opened in new window")
            img.open('popularity_bar_top10.png').show()
        else:
            print("Invalid Input")


x1 = range(5, 105, 10)
dispatcher = {1: show_df, 2: show_artist, 3: show_mode, 4: show_release_date, 5: show_key, 6: show_popularity, 7: show_duration,
              8: show_danceability, 9: show_energy, 10: show_loudness, 11: show_valence, 12: show_speechiness,
              13: show_acousticness, 14: show_instrumentalness, 15: show_liveness, 16: show_tempo}

choices = ['Q', 'q'] + list(range(1, 17)) + list(map(str, range(1, 17)))
choice = 0
if __name__ == '__main__':
    while choice not in ['Q', 'q']:
        print(main_menu)
        inp = input(">>> ")
        if inp in ['Q', 'q']: break
        if inp not in choices:
            print("Invalid Choice.\nRETRY")
            continue
        try:
            choice = int(inp)
        except ValueError:
            choice = inp
        except Exception as e:
            print(f"[ERROR] {e}")
            continue

        dispatcher[choice]()

    print("[END] Goodbye!")
