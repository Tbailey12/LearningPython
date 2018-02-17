import numpy as np
import json
import pandas as pd

filename = "ratings.json"


def read_ratings(file):
    """
    reads json with dict like data style
    :param file: json file
    :return: dict with data from json
    """
    with open(file, 'r') as file:
        file_data = file.read()

    json_data = json.loads(file_data)
    return json_data


def get_similarity_score(differences):
    """
    calculates the euclidean distance between a number of scores and returns an overall similarity
    :param differences: a list of differences between users
    :return: the similarity score 0-->1 with 1 being the same number
    """

    sum_of_squares = 0
    for diff in differences:
        sum_of_squares += np.power(diff, 2)

    similarity_score = 1 / (np.sqrt(sum_of_squares) + 1)
    return similarity_score


def get_differences(movies, user1, user2):
    """

    :param movies: a list of all movies being reviewed
    :param user1: the first user to compare
    :param user2: the second user to compare
    :return:
    """
    differences = list()
    for movie in movies:
        try:
            rating1 = user1.get_ratings()[movie]
            rating2 = user2.get_ratings()[movie]
        except KeyError:
            continue

        differences.append(abs(rating2 - rating1))

    return differences


class User:
    """
    User object used to store ratings for each user
    """

    def __init__(self, name, ratings):
        self.name = name
        self.ratings = ratings

    def get_name(self):
        return self.name

    def get_ratings(self):
        return self.ratings


if __name__ == "__main__":
    data = read_ratings(filename)
    movie_list = data['movies']

    user_list = list()

    # create a list of all user objects containing their reviews
    for key in data['ratings'].keys():
        user_list.append(User(key, data['ratings'][key]))

    # create a dataframe for storing similarity scores between users
    similarity_scores = pd.DataFrame(columns=[user.get_name() for user in user_list],
                                     index=[user.get_name() for user in user_list])

    # calculate similarity score between all users
    for user1 in user_list:
        for user2 in user_list:
            differences = get_differences(movie_list, user1, user2)
            score = get_similarity_score(differences)
            similarity_scores.loc[user1.get_name(), user2.get_name()] = score

    print(similarity_scores)
