# In a new file (we can call it api.py and store it in the same directory \
#like our previous notebook and pickle file model.p). 

# import Flask and jsonify
from flask import Flask, jsonify, request
# import Resource, Api and reqparser
from flask_restful import Resource, Api, reqparse
import pandas as pd
import numpy
import pickle

# Create a new flask app instance
app = Flask(__name__)
# Create the API object
api = Api(app)

# we need to create the same custom class we used in the model creation part. \
# The functions from that class are used in the model and stored in the pickle file we created earlier. \
# Therefore, the model needs to have access to the class during the scoring as well. \
# The accesses to other sklearn modules are provided automatically and we don't have to do anything \
# about them in the scoring file.

# Create a class for the API
class RawFeats:
    def __init__(self, feats):
        self.feats = feats

    def fit(self, X, y=None):
        pass


    def transform(self, X, y=None):
        return X[self.feats]

    def fit_transform(self, X, y=None):
        self.fit(X)
        return self.transform(X)
    
# Load model from pickle file
model = pickle.load( open("model.p", "rb"))

# Now, we need to create an endpoint where we can communicate with our ML model. \
# This time, we are going to use POST request

class Scoring(Resource):
    def post(self):
        json_data = request.get_json()
        df = pd.DataFrame(json_data.values(), index=json_data.keys()).transpose()
        # getting predictions from our model.
        # it is much simpler because we used pipelines during development
        res = model.predict_proba(df)
        # we cannot send numpt array as a result
        return res.tolist() 

# assign endpoint
api.add_resource(Scoring, '/scoring')

#The last thing to do is to create an application run when the file api.py is run directly

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=888)
