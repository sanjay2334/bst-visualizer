from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api
from binarytree import Node
from app.bst import BST
import random
import time 

app = Flask(__name__)
api = Api(app)

biglist = list(range(1, 30))

class MainResource(Resource):
    def get(self):
        # strip query params
        n = request.args.get('nodes')
        if n:
            n = n.strip().split(',')
            nodes = [int(e) for e in n]
            # print(nodes, nodes[0], nodes[1])
            range = request.args.get('range')
            shuffle = None 
            if range and range.lower() == 'true': 
                nodes[:] = biglist
                shuffle = "true"
            
            if not shuffle:
                shuffle = request.args.get('shuffle')

            if shuffle and shuffle.lower() == 'true':
                linearTree = random.choice([False, True, False, False, False])
                if linearTree:
                    nodes.sort()
                else:
                    random.shuffle(nodes)

            bst = BST()

            try:
                for n in nodes:
                    bst.binary_insert(int(n))
            except:
                return 'An error occurred, please double check your input!'

            response = make_response(bst.get_output(), 200)
            response.mimetype = 'text/plain'

        else:
            response = 'You must supply a comma delimited list of numbers in a \'nodes\' query param!'
        return response


api.add_resource(MainResource, '/')

if __name__ == '__main__':
    random.seed(time)
    app.run()
