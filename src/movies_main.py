import sys
from movie_class import load_basics
from rating_class import load_ratings
from query_handler import *
# importing class methods and timer


def main():
    # main file

    args = sys.argv

    if len(args) < 2:
        # setting up dicts

        print("reading data/title.basics.tsv into dict...")
        start = timer()
        movies = load_basics("data/title.basics.tsv")
        elapsed = timer() - start
        print('elapsed time (s):', elapsed, "\n")

        print("reading data/title.ratings.tsv into dict...")
        start = timer()
        ratings = load_ratings("data/title.ratings.tsv")
        elapsed = timer() - start
        print('elapsed time (s):', elapsed, "\n")
    else:

        print("reading data/small.basics.tsv into dict...")
        start = timer()
        movies = load_basics("data/small.basics.tsv")
        elapsed = timer() - start
        print('elapsed time (s):', elapsed, "\n")

        print("reading data/small.ratings.tsv into dict...")
        start = timer()
        ratings = load_ratings("data/small.ratings.tsv")
        elapsed = timer() - start
        print('elapsed time (s):', elapsed, "\n")

    print("Total movies: ", len(movies))
    print("Total ratings: ", len(ratings), "\n")

    for line in sys.stdin:
        # reading input
        line = line.strip()  # remove trailing newline
        query = line.split(" ")

        if query[0] == "LOOKUP":
            lookup(query, movies, ratings)
        elif query[0] == "CONTAINS":
            contains(query, movies)
        elif query[0] == "YEAR_AND_GENRE":
            year_and_genre(query, movies)
        elif query[0] == "RUNTIME":
            runtime(query, movies)
        elif query[0] == "MOST_VOTES":
            most_votes(query, movies, ratings)
        elif query[0] == "TOP":
            top(query, movies, ratings)


if __name__ == '__main__':
    main()
