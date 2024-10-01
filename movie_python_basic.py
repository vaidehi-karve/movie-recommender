# This is a py file

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from ast import literal_eval
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

"""
Steps:
    1. Open and read csv files 
    2. combine csv files

"""



# Step 1
# Opening and reading the csv file and capturing in dataframe df1, df2 and df3
df1=pd.read_csv('/Users/vaidehikarve/git_movie_recommender_project/movie-recommender/csv_db/movies_metadata.csv', low_memory = False)
df2=pd.read_csv('/Users/vaidehikarve/git_movie_recommender_project/movie-recommender/csv_db/keywords.csv')
