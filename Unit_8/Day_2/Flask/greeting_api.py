# import Flask and jsonify
from flask import Flask, jsonify

# import Resource, Api and reqparser
from flask_restful import Resource, Api, request

# create an application object 

app = Flask(__name__)

# create the API object
api = Api(app)

# Now that our API has been created, we need to add an endpoint. \
# We can do that by creating a class with the name Greet (any other name will work as well). \
# This class must inherit properties from the Resources class from the flask_restful module.

class Greet(Resource):
    def get(self):

        name = request.args.get('name')

        if name:
            greeting = f'Hello {name}!'
        else:
            greeting = 'Hello person without name!'

        # make json from greeting string 
        return jsonify(greeting=greeting)
    
    # Now that we have our class created, we need to assign an endpoint. \
    # The functionality of the Greet class will be available in the /greet endpoint.

    # assign endpoint
api.add_resource(Greet, '/greet')

# The last thing to do is to create an application run when the file greeting_api.py \
# is called directly (not imported as a module from another script).

if __name__ == '__main__':
    app.run(debug=True)
    