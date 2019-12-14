#!flask/bin/python
## Please run server with ./runit script to enable debug and enjoy pretty listing...
from flask import Flask, jsonify,  request, abort, make_response

app = Flask(__name__, 
            static_url_path='', static_folder='./')
            #static_folder='../')

# Create sample Customer list on the REST Server
customers = [
    {
        "id":1000,
        "firstname":"Francis",
        "lastname":"Adepoju",
        "gender":"M",
        "age":"67-99",
        "lastvisit":"05/11/2019",
        "product":"iPhone",
        "amountspent":2000
    },
    {
        "id":1001,
        "firstname":"Ann",
        "lastname":"Schmitz",
        "gender":"F",
        "age":"19-25",
        "lastvisit":"11/02/2018",
        "product":"Blender",
        "amountspent":250
    },
    {
        "id":1002,
        "firstname":"Philip",
        "lastname":"McGinley",
        "gender":"M",
        "age":"36-45",
        "lastvisit":"28/02/2019",
        "product":"Trainers",
        "amountspent":199
    }
]
# Server Generates Customer ID automatically
nextID = 1003

# Default method from server 
# curl -i http://localhost:5000
@app.route('/')
def index():
    return "Hello, Flask Server is running on port 5000 on local machine and also on the cloud at pythonAnywhere for the ...bigPROJECT...\n"

# Show all customers
# curl -i http://localhost:5000/customers
@app.route('/customers', methods=['GET'])
def get_customers():
    return jsonify({'customers':customers}) # json.dump(data, f, indent=4)

# Show a specific Customer
#curl -i http://localhost:5000/customer/100
@app.route('/customers/<int:id>', methods =['GET'])
def get_customer(id):
    foundCustomer = list(filter(lambda cus : cus['id'] == id , customers))
    if len(foundCustomer) == 0:
        return jsonify( { 'customer' : '' }),204
    return jsonify( { 'customer' : foundCustomer[0] })

# Create a Customer
# curl -i -H "Content-Type:application/json" -X POST -d '{"firstname":"Kolly","lastname":"Geene", "gender":"M", "age":41, "lastvisit":"12-12-2000", "product":"T-Shirt", "totalspent":99}' http://localhost:5000/customers
# curl -i -H "Content-Type:application/json" -X POST -d '{"id":202,"firstname":"Kolly","lastname":"Geene", "gender":"M", "age":41, "lastvisit":"12-12-2000", "product":"T-Shirt", "totalspent":89}' http://localhost:5000/customers
@app.route('/customers', methods=['POST'])
def create_customer():

    global nextID 
    
    if not request.json:
        abort(400)
    # if not 'id' in request.json:
    #     abort(400)

    customer = {
    "id":  nextID,
        "firstname": request.json['firstname'],
        "lastname":request.json['lastname'],
        "gender":  request.json['gender'],
        "age": request.json['age'],
        "lastvisit":request.json['lastvisit'],
        "product":request.json['product'],
        "amountspent":request.json['amountspent'],
    }
    nextID += 1
    customers.append(customer)
    return jsonify( {'customer':customer }),201

# Delete a customer
# curl -X DELETE http://localhost:5000/customers/101
@app.route('/customers/<int:id>', methods =['DELETE'])
def delete_customer(id):
    foundCustomer = list(filter (lambda cust : cust['id'] == id, customers))
    if len(foundCustomer) == 0:
        abort(404)
    customers.remove(foundCustomer[0])
    return  jsonify( { 'result':True })

# Update a Customer record
@app.route('/customers/<int:id>', methods =['PUT'])
def update_customer(id):
    foundCustomer=list(filter(lambda cust : cust['id'] == id, customers))
    if len(foundCustomer) == 0:
        abort(404)
    if not request.json:
        abort(400)
    
    if 'amountspent' in request.json and type(request.json['amountspent']) is not int:
        abort(400)
    if 'lastname' in request.json and type(request.json['lastname']) is not str:
        abort(400)
    if 'gender' in request.json and type(request.json['gender']) is not str:
        abort(400)
    if 'product' in request.json and type(request.json['product']) is not str:
        abort(400)
    if 'lastvisit' in request.json and type(request.json['lastvisit']) is not str:
        abort(400)

    foundCustomer[0]['firstname']   = request.json.get('firstname', foundCustomer[0]['firstname'])
    foundCustomer[0]['lastname']    = request.json.get('lastname',  foundCustomer[0]['lastname'])
    foundCustomer[0]['gender']      = request.json.get('gender',    foundCustomer[0]['gender'])
    foundCustomer[0]['age']         = request.json.get('age',       foundCustomer[0]['age'])
    foundCustomer[0]['lastvisit']   = request.json.get('lastvisit', foundCustomer[0]['lastvisit'])
    foundCustomer[0]['product']     = request.json.get('product',   foundCustomer[0]['product'])
    foundCustomer[0]['amountspent']  = request.json.get('amountspent',foundCustomer[0]['amountspent'])

    return jsonify( {'customer':foundCustomer[0]})


@app.errorhandler(404)
def not_found404(error):
    return make_response( jsonify( {'error':'Not found' }), 404)

@app.errorhandler(400)
def not_found400(error):
    return make_response( jsonify( {'error':'Bad Request' }), 400)

if __name__ == '__main__' :
    #app.run(debug= True)   this debug=True disables debug mode in VSC...
    app.run()