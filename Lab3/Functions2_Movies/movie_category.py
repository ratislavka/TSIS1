from movies_data import movies

category_inp = input("Enter a category: ")
category_inp = category_inp.lower()         # category_inp.lower() won't work because the lower() method
                                            # is not modifying the original category ,it’s creating a lowercase version for the comparison

def get_by_category(movie, category_inp):
    if movie['category'].lower() == category_inp:
        return movie['name']

for movie in movies:
    movie_name = get_by_category(movie, category_inp)
    if movie_name is not None:
        print(movie_name)
