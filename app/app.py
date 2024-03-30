from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np  # Import NumPy here

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for the entire app

# Load the trained model
filename = 'movie_popularity_model.pkl'
model = pickle.load(open(filename, 'rb'))

@app.route('/predict', methods=['POST'])
def predict_popularity():
    data = request.get_json(force=True)
    budget = data['budget']
    runtime = data['runtime']
    
    # Make prediction
    prediction = model.predict(np.array([[budget, runtime]]))  # Use NumPy here
    
    # Return the prediction
    return jsonify(popularity=prediction[0])

if __name__ == '__main__':
    app.run(debug=False)
