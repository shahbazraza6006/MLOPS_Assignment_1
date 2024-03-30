from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import pickle


# Load dataset
movies_df = pd.read_csv('tmdb_5000_movies.csv')

# Handling missing values in 'runtime'
movies_df['runtime'].fillna(movies_df['runtime'].mean(), inplace=True)

# Selecting features and target
X = movies_df[['budget', 'runtime']]
y = movies_df['popularity']

# Splitting the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training the model
model = RandomForestRegressor(n_estimators=10, random_state=42)
model.fit(X_train, y_train)

# Save the model to disk
filename = 'movie_popularity_model.pkl'
pickle.dump(model, open(filename, 'wb'))

# Load the trained model
model = pickle.load(open(filename, 'rb'))

print('Model training and saving completed successfully')