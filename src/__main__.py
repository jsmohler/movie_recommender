# from .scripts.basic_comparison import *
from .scripts.excel_parser import parse_to_dictionary
from .scripts.recommender import recommender
from .scripts.visualization import visualizeCorrelation

workbook_path = 'src/data/Sample_Movie_Ratings.xlsx'

user_ratings = parse_to_dictionary(workbook_path)

k = 3
n = 5
metric = 'pearson'

r = recommender(user_ratings, k=k, n=n, metric=metric)

for user in ['Zak', 'Brian', 'Patrick C']:
    print('\n{0}\'s {1} nearest neighbors: '.format(user, k), r.computeNearestNeighbor(user)[:k], '. They recommend ', r.recommend(user))

# visualizeCorrelation(user_ratings, "Zak", "Vanessa")