import csv

def read_movies():
    with open('film.csv', 'rb') as f:
        reader = csv.reader(f, delimiter=';')
        rows = [row for row in reader]
    # Question: why am I splitting the 0th row from the rest?
    return rows[0], rows[2:]


def get_short_movies(movies):
    """
    Take the movies list and filter out those
    that are longer than 120 minutes.
    """
    short_movies = []
    for movie in movies:
        # Let's try to integer-ify the movie duration,
        # since it is a string to begin with
        try:
            # the 1-th index is the Length of the movie
            # Let's check that the duration is less than 120 minutes
            if int(movie[1]) < 120:
                # if so, then add movie to the short_movies list
                short_movies.append(movie)
        # if it throws an error, then do what's in the
        # except block, which is just continue
        except:
            continue
    # Finally, return short_movies
    return short_movies

def get_popular_movies(movies):
    """
    Take the movies list and filter out those
    that do not exceed popularity score of 40
    """
    popular_movies = []
    for movie in movies:
        # Let's try to integer-ify the movie popularity,
        # since it is a string to begin with
        try:
            # the 7-th index of movie is the Popularity
            if int(movie[7]) > 40:
                # if so, then add movie to the short_movies list
                popular_movies.append(movie)
        except:
            continue
    # Finally, return short_movies
    return popular_movies


def recommend_from(movies):
    """
    Recommends a random element from the movies list.
    """
    return random.choice(movies)