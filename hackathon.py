#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
data = pd.read_csv(r'C:\Users\Uday Kumar V\Downloads\movie_data\ratings.csv')
print(data.shape)


# In[ ]:


ratings_data = pd.read_csv(r'C:\Users\Uday Kumar V\Downloads\movie_data\ratings.csv')
movie_ratings_count = ratings_data.groupby('movieId').size()
most_rated_movie_id = movie_ratings_count.idxmax()
most_rated_count = movie_ratings_count.max()

print(most_rated_movie_id)
print(most_rated_count)


# In[ ]:


movies_data = pd.read_csv(r'C:\Users\Uday Kumar V\Downloads\movie_data\movies.csv')
merged_data = pd.merge(ratings_data, movies_data, on='movieId')

movie_ratings_count = merged_data.groupby('movieId').size()
most_rated_movie_id = movie_ratings_count.idxmax()
most_rated_count = movie_ratings_count.max()
most_rated_movie_title = movies_data[movies_data['movieId'] == most_rated_movie_id]['title'].values[0]

print(most_rated_movie_title)
print(most_rated_count)


# In[ ]:


movies_data = pd.read_csv(r'C:\Users\Uday Kumar V\Downloads\movie_data\movies.csv')
tags_data = pd.read_csv(r'C:\Users\Uday Kumar V\Downloads\movie_data\tags.csv')


# In[ ]:


movie_id = movies_data[movies_data['title'] == "Matrix, The (1999)"]['movieId'].values[0]


# In[ ]:


tags_for_movie = tags_data[tags_data['movieId'] == movie_id]
print(tags_for_movie['tag'].unique())


# In[ ]:


movie_id = movies_data[movies_data['title'] == "Terminator 2: Judgment Day (1991)"]['movieId'].values[0]
ratings_for_movie = ratings_data[ratings_data['movieId'] == movie_id]
average_rating = ratings_for_movie['rating'].mean()

print(average_rating)


# In[ ]:


import matplotlib.pyplot as plt
movies_data = pd.read_csv(r'C:\Users\Uday Kumar V\Downloads\movie_data\movies.csv')
ratings_data = pd.read_csv(r'C:\Users\Uday Kumar V\Downloads\movie_data\ratings.csv')
movie_id = movies_data[movies_data['title'] == "Fight Club (1999)"]['movieId'].values[0]

ratings_for_movie = ratings_data[ratings_data['movieId'] == movie_id]
plt.figure(figsize=(10, 6))
plt.hist(ratings_for_movie['rating'], bins=range(1, 6), edgecolor='black', alpha=0.7)
plt.title('Distribution of User Ratings for "Fight Club (1999)"')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.xticks(range(1, 6))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


# In[ ]:


ratings_grouped = ratings_data.groupby('movieId').agg(
    rating_count=('rating', 'size'),
    average_rating=('rating', 'mean')
).reset_index()

movies_with_ratings = pd.merge(movies_data, ratings_grouped, on='movieId')
movies_filtered = movies_with_ratings[movies_with_ratings['rating_count'] > 50]
most_popular_movie = movies_filtered.loc[movies_filtered['average_rating'].idxmax()]
print(most_popular_movie)


