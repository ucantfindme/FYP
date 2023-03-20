import pandas as pd
d=dict()
df1=pd.read_csv('csv-data/movie.csv')
df2=pd.read_csv('csv-data/movie_map.csv')
print(len(df1),len(df2))
for index, row in df1.iterrows():
    mv=row['movie_title']
    yr=row['year']
    gen=row['genre']
    syn=row['synopsis']
    cast=row['cast']
    d[mv]=[yr,gen,cast,syn]
for index, row in df2.iterrows():
    mv=row['Movie']
    if mv in d:
        d[mv].append(row['Photo_url'])
c=0
from accounts.models import Movie
for i in d:
    if len(d[i])==7:
        try:
            m=Movie(
                title=i,
                year=d[i][0],
                genre=d[i][1],
                cast=d[i][2],
                description=d[i][3],
                p1=d[i][4],
                p2=d[i][5],
                p3=d[i][6]
            )
            m.save()
        except:
            pass
print(c)