from movies_data import movies

def high_score(movie):
    if movie['imdb'] > 5.5:
        return movie['name']

for movie in movies:
    if high_score(movie) is not None:
        print(high_score(movie))