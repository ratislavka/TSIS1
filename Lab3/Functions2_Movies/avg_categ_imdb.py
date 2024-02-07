from movies_data import movies

category_inp = input("Enter a category: ")
category_inp = category_inp.lower()

def avg_category_score(movies):
    total_score = 0
    movie_num = 0
    for movie in movies:
        if movie['category'].lower() == category_inp:
            movie_num += 1
            total_score += movie['imdb']
    avg_score = total_score/movie_num
    return avg_score

print(avg_category_score(movies))

