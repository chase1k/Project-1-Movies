from dataclasses import dataclass

from movie_class import Movie
from rating_class import Rating

# This class is neccessary in order to sort by both votes and primary title (also rating for top)
# There was another way to sort using lambda but, I struggled until this worked
@dataclass
class MV:
    tconst: str
    primaryTitle: str
    numVotes: int
    averageRating: float


def make_movie(tc: str, titl: str, votes: int):
    """
    :param tc: tconst
    :param titl: primaryTitle
    :param votes: numVotes
    :return: MV object without rating specified
    """
    tconst = tc
    primaryTitle = titl
    numVotes = votes

    return MV(tconst, primaryTitle, numVotes, 0.0)


def make_movie_with_rats(tc: str, titl: str, votes: int, ratin: float):
    """
    :param tc: tconst
    :param titl: primaryTitle
    :param votes: numVtoes
    :param ratin: averageRating
    :return: MV object with average rating specified
    """
    tconst = tc
    primaryTitle = titl
    numVotes = votes
    averageRating = ratin

    return MV(tconst, primaryTitle, numVotes, averageRating)
