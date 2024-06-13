from Util import card


def genres(movies):
    return {genre for movie in movies for genre in movie.genres}


def actors(movies):
    return {actor for movie in movies for actor in movie.actors}


def repeat_consecutive(xs, k):
    return [x for x in xs for _ in range(k)]
