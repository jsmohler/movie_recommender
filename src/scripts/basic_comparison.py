#
#  FILTERINGDATA.py
#
#  Code file for the book Programmer's Guide to Data Mining
#  http://guidetodatamining.com
#  Ron Zacharski
#

from math import sqrt
from enum import Enum


def manhattan(rating1, rating2):
    """Computes the Manhattan distance. Both rating1 and rating2 are dictionaries
       of the form {'The Strokes': 3.0, 'Slightly Stoopid': 2.5}"""
    distance = 0
    commonRating = False
    for key in rating1:
        if key in rating2:
            distance += abs(rating1[key] - rating2[key])
            commonRating = True
    if commonRating:
        return distance
    else:
        return -1  # Indicates no ratings in common


def sortNeighborsByNearest(username, user_ratings):
    """creates a sorted list of users based on their distance to username"""
    distances = []
    for user in user_ratings:
        if user != username:
            distance = manhattan(user_ratings[user], user_ratings[username])
            distances.append((distance, user))
    # sort based on distance -- closest first
    distances.sort()
    return distances


def recommend(username, user_ratings):
    """Give list of recommendations"""
    # first find nearest neighbor
    nearest = sortNeighborsByNearest(username, user_ratings)[0][1]

    recommendations = []
    # now find movies neighbor rated that user didn't
    neighborRatings = user_ratings[nearest]
    givenUserRatings = user_ratings[username]
    for movie in neighborRatings:
        if not movie in givenUserRatings:
            recommendations.append((movie, neighborRatings[movie]))
    # using the fn sorted for variety - sort is more efficient
    return sorted(recommendations, key=lambda movieTuple: movieTuple[1], reverse=True)
