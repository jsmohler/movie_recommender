# from .scripts.basic_comparison import *
from .scripts.excel_parser import parse_to_dictionary, visualize
from .scripts.recommender import recommender

workbook_path = 'src/data/Sample_Movie_Ratings.xlsx'

user_ratings = parse_to_dictionary(workbook_path)

# visualize(user_ratings)
# print(user_ratings);

r = recommender(user_ratings)

print(r.recommend('Brian'))