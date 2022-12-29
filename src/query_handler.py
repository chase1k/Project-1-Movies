import operator
from timeit import default_timer as timer
from mv_class import *


def lookup(query, movies, ratings):
    """
    :param query: input from config in a list separated by " "
    :param movies: dict of all movie objects
    :param ratings: dict of all rating objects
    :return: None
    """

    # Looks up movie and rating in dict based on title type
    print("processing: LOOKUP", query[1])
    start = timer()

    if query[1] not in movies:
        print("\tMovie not found!")

        if query[1] not in ratings:
            print("\tRating not found!")

        elapsed = timer() - start
        print('elapsed time (s):', elapsed)
        return

    m = movies.get(query[1])
    r = ratings.get(query[1])
    # organized movie and rating for simpler code

    print("\tMOVIE: Identifier:", m.tconst + ", Title:", m.primaryTitle +
          ", Type:", m.titleType + ", Year:", str(m.startYear) + ", Runtime:",
          str(m.runtimeMinutes) + ", Genres:", m.genres)
    print("\tRATING: Identifier:", r.tconst + ", Rating:",
          str(r.averageRating) + ", Votes:", str(r.numVotes))
    elapsed = timer() - start
    print("elapsed time (s):", elapsed, "\n")


def contains(query, movies):
    """
    :param query: input from config in a list separated by " "
    :param movies: dict of all movie objects
    :return: None
    """
    # Checks if provided text is contained in a title type
    print("processing: CONTAINS", query[1], ' '.join(query[2:]))

    start = timer()
    printed = False
    for m in movies.values():

        if query[1] in str(m.titleType) and ' '.join(query[2:]) in str(m.primaryTitle):
            printed = True
            print("\tIdentifier:", m.tconst + ", Title:", m.primaryTitle +
                  ", Type:", m.titleType + ", Year:", str(m.startYear) + ", Runtime:",
                  str(m.runtimeMinutes) + ", Genres:", m.genres)
    if not printed:
        print("\tNo match found!")

    elapsed = timer() - start
    print('elapsed time (s):', elapsed, "\n")
    return


def year_and_genre(query, movies):
    """
    :param query: input from config in a list separated by " "
    :param movies: dict of all movie objects
    :return: None
    """

    # Checks for movies in provided year and genre in a title type
    print("processing: YEAR_AND_GENRE", query[1], query[2], ' '.join(query[3:]))

    start = timer()
    dictTitle = {}

    for m in movies.values():

        if query[1] in str(m.titleType) and query[2] in str(m.startYear) and query[3] in str(m.genres):
            dictTitle[m.primaryTitle] = m

    if dictTitle == {}:
        print("\tNo match found!")

    listTitle = list(dictTitle.keys())
    listTitle.sort()

    for m in listTitle:
        m = dictTitle[m]
        print("\tIdentifier:", m.tconst + ", Title:", m.primaryTitle +
              ", Type:", m.titleType + ", Year:", str(m.startYear) + ", Runtime:",
              str(m.runtimeMinutes) + ", Genres:", m.genres)

    elapsed = timer() - start
    print('elapsed time (s):', elapsed, "\n")
    return


def runtime(query, movies):
    """
    :param query: input from config in a list separated by " "
    :param movies: dict of all movie objects
    :return: None
    """

    # Checks for movies withing provided range of runtimes in a title type
    print("processing: RUNTIME", query[1], query[2], query[3])

    start = timer()
    dictTime = {}

    for m in movies.values():

        if query[1] in str(m.titleType) and int(query[2]) <= m.runtimeMinutes <= int(query[3]):
            dictTime[m.tconst] = m

    if dictTime == {}:
        print("\tNo match found!")

    listTime = list(dictTime.values())

    listTime.sort(key=operator.attrgetter('primaryTitle'))
    listTime.sort(key=operator.attrgetter('runtimeMinutes'), reverse=True)

    for m in listTime:
        m = dictTime[m.tconst]
        print("\tIdentifier:", m.tconst + ", Title:", m.primaryTitle +
              ", Type:", m.titleType + ", Year:", str(m.startYear) + ", Runtime:",
              str(m.runtimeMinutes) + ", Genres:", m.genres)

    elapsed = timer() - start
    print('elapsed time (s):', elapsed, "\n")
    return


def most_votes(query, movies, ratings):
    """
    :param query: input from config in a list separated by " "
    :param movies: dict of all movie objects
    :param ratings: dict of all rating objects
    :return: None
    """

    # Checks if provided text is contained in a movie title
    print("processing: MOST_VOTES", query[1], query[2])

    start = timer()
    listMovies = []
    listMVs = []

    for m in movies.values():

        if query[1] in str(m.titleType):
            if ratings.get(m.tconst):
                listMovies.append(m)
            elif query[1] not in str(m.titleType):
                print("No match found!")
                return

    for movie in listMovies:
        tc = movie.tconst
        titl = movie.primaryTitle
        votes = int(ratings[tc].numVotes)
        listMVs.append(make_movie(tc, titl, votes))

    listMVs.sort(key=operator.attrgetter('primaryTitle'))
    listMVs.sort(key=operator.attrgetter('numVotes'), reverse=True)

    if int(query[2]) > len(listMVs):
        query[2] = len(listMVs)

    if len(listMVs) == 0:
        print("\t\tNo match found!")
        elapsed = timer() - start
        print('elapsed time (s):', elapsed, "\n")
        return

    for i in range(int(query[2])):

        mkey = listMVs[i].tconst
        m = movies[mkey]
        print("\t" + str(i+1) + ". VOTES:" + str(listMVs[i].numVotes) + ", MOVIE: Identifier:",
              m.tconst + ", Title:", m.primaryTitle +
              ", Type:", m.titleType + ", Year:", str(m.startYear) + ", Runtime:",
              str(m.runtimeMinutes) + ", Genres:", m.genres)

    elapsed = timer() - start
    print('elapsed time (s):', elapsed, "\n")
    return


def top(query, movies, ratings):
    """
    :param query: input from config in a list separated by " "
    :param movies: dict of all movie objects
    :param ratings: dict of all rating objects
    :return:
    """

    # Checks if provided text is contained in a movie title
    print("processing: TOP", query[1], query[2], query[3], query[4])

    start = timer()
    listMovies = []
    listMVs = []

    for m in movies.values():

        if query[1] in str(m.titleType):
            if ratings.get(m.tconst) and ratings[m.tconst].numVotes >= 1000:
                listMovies.append(m)
            elif query[1] not in str(m.titleType):
                print("No match found!")
                return

    for movie in listMovies:
        tc = movie.tconst
        titl = movie.primaryTitle
        votes = int(ratings[tc].numVotes)
        ratin = float(ratings[tc].averageRating)
        listMVs.append(make_movie_with_rats(tc, titl, votes, ratin))

    # print(listMVs)

    listMVs.sort(key=operator.attrgetter('primaryTitle'))
    listMVs.sort(key=operator.attrgetter('numVotes'), reverse=True)
    listMVs.sort(key=operator.attrgetter('averageRating'), reverse=True)

    # print(listMVs)

    if int(query[2]) > len(listMVs):
        query[2] = len(listMVs)

    listVMs = listMVs

    for i in range(int(query[4])-int(query[3])+1):
        print("\tYEAR: " + str(i + int(query[3])))

        listMVs = listVMs
        listToPrint = []

        for j in listMVs:
            year = int(movies[j.tconst].startYear)
            # print(yearDif)
            if (i + int(query[3])) == year:
                # listMVs.pop(listMVs.index(j))
                listToPrint.append(j)
        # makes list for within years
        if len(listToPrint) == 0:
            print("\t\tNo match found!")
            continue

        # print(listToPrint)
        for j in range(int(query[2])):
            if not (0 <= j < len(listToPrint)):
                continue
            mkey = listToPrint[j].tconst
            m = movies[mkey]
            print("\t\t" + str(j+1)
                  + ". RATING: " + str(listToPrint[j].averageRating)
                  + ", VOTES:" + str(listToPrint[j].numVotes)
                  + ", MOVIE: Identifier:", m.tconst
                  + ", Title:", m.primaryTitle
                  + ", Type:", m.titleType
                  + ", Year:", str(m.startYear)
                  + ", Runtime:", str(m.runtimeMinutes)
                  + ", Genres:", m.genres)

    elapsed = timer() - start
    print('elapsed time (s):', elapsed, "\n")
    return
