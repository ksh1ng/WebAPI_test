'''
Title: Innerproduct API using flask
Name: Kshing
Date: <2020.3.13>
Description:
ref to <innerproduct.pdf>
Todo: P8, P9, P11
'''

from flask import Flask, jsonify, request
import numpy as np

#建立app
app = Flask(__name__)

number_of_requests = {}
number_of_errors = {}

#針對所需的route新增對應建立view function用來處理使用者的request
'''
POST參數(json): { "x": [1, 2, 3], "y": [4, 5, 6]}
'''
@app.route('/innerproduct', methods=['POST','GET'])
def innerproduct():
    
    path = "innerproduct"
    if (request.method == 'POST'):
        #request log
        if path not in number_of_requests:
            number_of_requests['innerproduct'] = 0

        number_of_requests['innerproduct'] += 1

        some_json = request.get_json() #dict type
        #print(f"some_json={type(some_json)}")

        vector_a = some_json['x']
        vector_b = some_json['y']

        #P6 Check length of incoming array
        if (len(vector_a)  >= 1 and len(vector_a)  <= 50 ) and (len(vector_a) == len(vector_b) ):
            inner_product_result = np.dot(vector_a, vector_b)
            return jsonify({"xTy": int(inner_product_result)}), 200
        else:
            #error log
            if  path not in number_of_errors:
                number_of_errors[path] = 0

            number_of_errors[path] += 1

            return jsonify({"error": {"type": "format error"} }), 200

    else:
        return jsonify({"about": 'InnerProduct API'})


@app.route('/info/', methods=['GET'])
def get_info():
    return jsonify({'number_of_requests': number_of_requests, 'number_of_errors': number_of_errors,})

# curl -H "Content-Type: application/json; charset=utf-8" -X POST --data '{"name":"xyz", "address":"addr xyz"}' http://127.0.0.1:5000/


if __name__ == '__main__':
    app.debug = True
    app.run()
