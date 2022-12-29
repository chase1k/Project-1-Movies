from dataclasses import dataclass


@dataclass (frozen=True)
class Movie:
    tconst: str
    titleType: str
    primaryTitle: str
    originalTitle: str
    startYear: int
    endYear: int = 0
    runtimeMinutes: int = 0
    genres: str = ""


def load_basics(filename: str):
    """
    :param filename: basics tsv file
    :return: dict of movie objects
    """
    movie_list = {}

    with open(filename, encoding='utf-8') as f:

        for line in f:

            movie = line.split("\t")
            if movie[0] == "tconst":
                continue

            if int(movie[4]) == 1:
                continue

            for i in range(5, 8):
                if movie[i] == '\\N':
                    movie[i] = 0

            if movie[8] == '\\N\n':
                movie[8] = 'None\n'

            movie_list.update(
                {movie[0]: Movie(tconst=str(movie[0]), titleType=str(movie[1]), primaryTitle=str(movie[2]),
                                 originalTitle=str(movie[3]), startYear=int(movie[5]), endYear=int(movie[6]),
                                 runtimeMinutes=int(movie[7]), genres=str(movie[8])[:-1])})
    return movie_list
