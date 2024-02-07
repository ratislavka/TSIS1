from movies_data import movies

def avg_imdb(movies):
    movie_num = len(movies)
    total_score = 0
    for movie in movies:
        total_score += movie['imdb']
    avg_score = total_score/movie_num
    return avg_score

print(avg_imdb(movies))

