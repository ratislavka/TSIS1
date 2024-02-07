from movies_data import movies

def high_score(movie):
    if movie['imdb'] > 5.5:
        return True
    else:
        return False

for movie in movies:
    print(movie['name'], high_score(movie))

