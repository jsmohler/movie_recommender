from .scripts.basic_comparison import *
from .scripts.excel_parser import *
# from .scripts.recommender import *

workbook_path = 'src/data/Sample_Movie_Ratings.xlsx'

user_ratings = parse_to_dictionary(workbook_path)

visualize(user_ratings)