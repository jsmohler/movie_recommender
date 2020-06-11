exec(open('recommendation.py').read())

pip freeze > requirements.txt
pip install -r requirements.txt