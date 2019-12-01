#!flask/bin/python
## Please run server with ./runit script to enable debug and enjoy pretty listing...
from flask import Flask, jsonify,  request, abort, make_response
from customerDAO import customerDAO

app = Flask(__name__, 
            static_url_path='', static_folder='./')
            #static_folder='../')

# # Create sample Customer list in MSQL Server

# Default method from server 
# curl -i http://localhost:5000
@app.route('/')
def index():
    return "Hello, Flask Server is running on port 5000 on local machine and also on the cloud at pythonAnywhere for the ...bigPROJECT...\n"

# Show all customers
# curl -i http://localhost:5000/customers
@app.route('/customers', methods=['GET'])
def get_customers():
    results = customerDAO.getAll()
    return jsonify(results)         # json.dump(data, f, indent=4)

# Show a specific Customer
#curl -i http://localhost:5000/customer/100
@app.route('/customers/<int:id>', methods =['GET'])
def get_customer(id):
    foundCustomer = customerDAO.findByID(id)
    # if len(foundCustomer) == 0:
    return jsonify(foundCustomer)
    # return jsonify( { 'customer' : foundCustomer[0] })

# Create a Customer
# curl -i -H "Content-Type:application/json" -X POST -d '{"firstname":"Kolly","lastname":"Geene", "gender":"M", "age":41, "lastvisit":"12-12-2000", "product":"T-Shirt", "totalspent":99}' http://localhost:5000/customers
# curl -i -H "Content-Type:application/json" -X POST -d '{"id":202,"firstname":"Kolly","lastname":"Geene", "gender":"M", "age":41, "lastvisit":"12-12-2000", "product":"T-Shirt", "totalspent":89}' http://localhost:5000/customers
@app.route('/customers', methods=['POST'])
def create_customer():

    # global nextID 
    
    if not request.json:
        abort(400)
    # if not 'id' in request.json:
    #     abort(400)

    customer = {
    # "id":  nextID,
        "firstname": request.json['firstname'],
        "lastname":request.json['lastname'],
        "gender":  request.json['gender'],
        "age": request.json['age'],
        "lastvisit":request.json['lastvisit'],
        "product":request.json['product'],
        "amountspent":request.json['amountspent'],
    }
    values =(customer['firstname'],customer['lastname'],customer['gender'],
            customer['age'],customer['lastvisit'],customer['product'],customer['amountspent'])

    newId = customerDAO.create(values)
    customer['id'] = newId
    return jsonify(customer)

# Delete a customer
# curl -X DELETE http://localhost:5000/customers/101
@app.route('/customers/<int:id>', methods =['DELETE'])
def delete_customer(id):
    # foundCustomer = list(filter (lambda cust : cust['id'] == id, customers))
    # if len(foundCustomer) == 0:
    #     abort(404)
    customerDAO.delete(id)
    return  jsonify( { 'Deleted OK':True })

# Update a Customer record
@app.route('/customers/<int:id>', methods =['PUT'])
def update_customer(id):
    foundCustomer=customerDAO.findByID(id)
    if not foundCustomer:
        abort(404)

    if not request.json:
        abort(400)
    
    reqJson = request.json
    if 'amountspent' in reqJson and type(reqJson['amountspent']) is not float:
        abort(400)
    # if 'lastname' in reqJson and type(reqJson['lastname']) is not str:
    #     abort(400)
    # if 'gender' in reqJson and type(reqJson['gender']) is not str:
    #     abort(400)
    # if 'product' in reqJson and type(reqJson['product']) is not str:
    #     abort(400)
    # if 'lastvisit' in reqJson and type(reqJson['lastvisit'] ) is not str:
    #     abort(400)

    if 'firstname' in reqJson:
        foundCustomer['firstname'] = reqJson['firstname']
    if 'lastname' in reqJson:
        foundCustomer['lastname'] = reqJson['lastname']
    if 'gender' in reqJson:
        foundCustomer['gender'] = reqJson['gender']
    if 'age' in reqJson:
        foundCustomer['age'] = reqJson['age']
    if 'lastvisit' in reqJson:
        foundCustomer['lastvisit'] = reqJson['lastvisit']
    if 'product' in reqJson:
        foundCustomer['product'] = reqJson['product']
    if 'amountspent' in reqJson:
        foundCustomer['amountspent'] = reqJson['amountspent']
    values = (foundCustomer['id'],foundCustomer['firstname'],foundCustomer['lastname'],
              foundCustomer['gender'],foundCustomer['age'],foundCustomer['lastvisit'],
              foundCustomer['product'],foundCustomer['amountspent'])
    customerDAO.update(values)
    return jsonify(foundCustomer)


# @app.errorhandler(404)
# def not_found404(error):
#     return make_response( jsonify( {'error':'Not found' }), 404)

# @app.errorhandler(400)
# def not_found400(error):
#     return make_response( jsonify( {'error':'Bad Request' }), 400)

if __name__ == '__main__' :
    #app.run(debug= True)   this debug=True disables debug mode in VSC...
    app.run()