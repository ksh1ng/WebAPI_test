'''
Title: Innerproduct API using flask
Name: Kshing
Date: <2020.3.13>
Description:ref to <innerproduct.pdf>
'''
from flask import Flask, jsonify, request
import numpy as np

#create app
app = Flask(__name__)

#for logging number of requests/errors
number_of_requests = {}
number_of_errors = {}


#create view function for handling POST/GET request through /innerproduct
'''
POST payload(json): { "x": [1, 2, 3], "y": [4, 5, 6]}
Return(json): {"xTy": 1*4+2*5+3*6}
How to use: 1.curl -i -X POST <your domain>/innerproduct/ -H "Content-Type: application/json; charset=utf-8" -d @<input json file path>
            2.curl -H "Content-Type: application/json; charset=utf-8" -X POST --data '{ "x": <array>, "y": <array>}' <your domain>/innerproduct/
'''
@app.route('/innerproduct/', methods=['POST','GET'])
def innerproduct():
    path = "innerproduct"

    if (request.method == 'POST'):

        #logging number of requests
        if path not in number_of_requests:
            number_of_requests['innerproduct'] = 0

        number_of_requests['innerproduct'] += 1

        #do innerproduct with two input vectors
        input_vectors = request.get_json() #dict type
        vector_a = input_vectors['x']
        vector_b = input_vectors['y']

        #Check length of incoming array
        if (len(vector_a)  >= 1 and len(vector_a)  <= 50 ) and (len(vector_a) == len(vector_b) ):
            inner_product_result = np.dot(vector_a, vector_b)
            return jsonify({"xTy": int(inner_product_result)}), 200
        else:
            #logging number of errors
            if  path not in number_of_errors:
                number_of_errors[path] = 0

            number_of_errors[path] += 1

            return jsonify({"error": {"type": "format error"} }), 200

    else:
        return jsonify({"about": 'InnerProduct API', "HowToUse": "curl -i -X POST <your domain>/innerproduct/ -H 'Content-Type: application/json; charset=utf-8' -d @<input json file path>"}), 200

#create view function for handling GET request through /info/
'''
How to use: curl <your domain>/info/
'''
@app.route('/info/', methods=['GET'])
def get_info():
    return jsonify({'number_of_requests': number_of_requests, 'number_of_errors': number_of_errors,})


if __name__ == '__main__':
    app.debug = True
    app.run()
