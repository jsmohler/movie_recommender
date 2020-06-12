# from .scripts.basic_comparison import *
from .scripts.excel_parser import parse_to_dictionary
from .scripts.recommender import recommender
from .scripts.visualization import visualizeCorrelation

workbook_path = 'src/data/Sample_Movie_Ratings.xlsx'

user_ratings = parse_to_dictionary(workbook_path)