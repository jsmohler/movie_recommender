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
        return -1 #Indicates no ratings in common

def euclidean(rating1, rating2):
    """Computes the Manhatten or Euclidean distance using Minkowski generalization. Both rating1 and rating2 are dictionaries
       of the form {'The Strokes': 3.0, 'Slightly Stoopid': 2.5}"""
    distance = 0
    commonRating = False
    for key in rating1:
        if key in rating2:
            distance += abs(rating1[key] - rating2[key]) ** 1/2
            commonRating = True
    if commonRating:
        return distance ** 1/2
    else:
        return -1 #Indicates no ratings in common


def minkowski(rating1, rating2, r):
    """Computes the Euclidean distance. Both rating1 and rating2 are dictionaries
       of the form {'The Strokes': 3.0, 'Slightly Stoopid': 2.5}"""
    distance = 0
    commonRating = False
    for key in rating1:
        if key in rating2:
            distance += abs(rating1[key] - rating2[key]) ** 1/r
            commonRating = True
    if commonRating:
        return distance ** 1/r
    else:
        return -1 #Indicates no ratings in common

def pearson(rating1, rating2):
    sum_xy = 0
    sum_x = 0
    sum_y = 0
    sum_x2 = 0
    sum_y2 = 0
    n = 0
    for key in rating1:
        if key in rating2:
            n += 1
            x = rating1[key]
            y = rating2[key]
            sum_xy += x * y
            sum_x += x
            sum_y += y
            sum_x2 += pow(x, 2)
            sum_y2 += pow(y, 2)
    # now compute denominator
    denominator = sqrt(sum_x2 - pow(sum_x, 2) / n) * sqrt(sum_y2 - pow(sum_y, 2) / n)
    if denominator == 0:
        return 0
    else:
        return (sum_xy - (sum_x * sum_y) / n) / denominator
            
def computeNearestNeighbor(username, users):
    """creates a sorted list of users based on their distance to username"""
    distances = []
    for user in users:
        if user != username:
            distance = manhattan(users[user], users[username])
            distances.append((distance, user))
    # sort based on distance -- closest first
    distances.sort()
    return distances

def recommend(username, users):
    """Give list of recommendations"""
    # first find nearest neighbor
    nearest = computeNearestNeighbor(username, users)[0][1]

    recommendations = []
    # now find movies neighbor rated that user didn't
    neighborRatings = users[nearest]
    userRatings = users[username]
    for movie in neighborRatings:
        if not movie in userRatings:
            recommendations.append((movie, neighborRatings[movie]))
    # using the fn sorted for variety - sort is more efficient
    return sorted(recommendations, key=lambda movieTuple: movieTuple[1], reverse = True)