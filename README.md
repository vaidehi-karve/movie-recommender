# Movie Recommendation System

Currently a work in progress, updates coming soon :)

# Description
I'm working on building a movie recommendation system based on demographic, content-based, and collaborative filtering. The final goal of this project is to generate age-specific recommendations for users ages in varying age groups, _without_ being given any information about the users themselves. I hope to accomplish this through genre analysis and clustering techniques as well as build on the three difference recommendation systems listed earlier.

This project is done in Python, and will be using the following libraries:
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* ast (Python module)
* surprise (Python scikit)


Here is a brief overview of each of the three movie recommendation systems.

### 1. Demographic Filtering
Demographic filtering is the most straight-forward of the recommendation systems I will be covering. As the name suggests, it is based solely on the demographics of the users (such as gender, ethinicity, age, etc.). The general idea is that members belonging to the same groups tend to like the same things - including movies. Obtaining user information, however, can be challenging, and it is something that this dataset lacks. In this case, my demographic filtering is somewhat broad and will be based on the average review and the number of review that each movie is given. In other words, the demographic I will be using is the entire population - no specific groups. **_The end goal of this project, however, is to recommend movies based on age group - which I will do without any user information._**

### 2. Content-based Filtering
While content-based filtering is 

### 3. Collaborative Filtering
Collaborative filtering is 


I will be using a dataset of 5,000 movies to 
