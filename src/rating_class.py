from dataclasses import dataclass


@dataclass (frozen=True)
class Rating:
    tconst: str
    averageRating: float
    numVotes: int


def load_ratings(filename: str):
    """
    :param filename: rating tsv file
    :return: dict of ratings objects
    """
    rating_list = {}

    with open(filename, encoding='utf-8') as f:
        for line in f:

            rats = line.split("\t")
            if rats[0] == "tconst":
                continue

            rating_list.update({rats[0]: Rating(tconst=(rats[0]), averageRating=float(rats[1]), numVotes=int(rats[2]))})

    return rating_list
