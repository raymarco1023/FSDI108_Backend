from flask import Flask, abort
from mock_data import catalog
from about_me import me, test
import json
# create the server/app
app = Flask("server")


@app.route("/", methods=["get"])
def home_page():
    return "Under Constructions!"


@app.route("/test")
def test():
    return "Test Test"


@app.route("/about")
def about():
    return "Ray"


@app.route("/address")
def get_address():
    test()
    me = {
        "fname": "Bruce",
        "lname": "Wayne",
        "age": 45,
        "hobbies": ["Outdoor", "gym"],
        "current_city": {
            "city": "Las Vegas",
            "street": "Las Vegas Blvd"
        }
    }
    address = me["current_city"]
    # return(address["street"] + " " + address["city"])
    return f"{address['stree']} {address['city']}"

###############################################
############ API Endpoint #####################
###############################################


@app.route9("/api/catalog")
def get_catalog():
    return json.dumps(catalog)

# get /api/catalog/ count
# return the num of products


@app.route("/api/catalog/count")
def get_count():
    count = len(catalog)
    return json.dumps(count)

# get / api/catalog/count
# return the sum of all prices


@app.route("/api/catalog/sum")
def get_sum():
    total = 0
    for prod in catalog:
        total += prod["price"]

    res = f"$ {total}"
    return json.dumps(total)

#get /api/product/id
# get a produce by its id


@app.route("/api/product/<id>")
def get_product(id):
    for prod in catalog:
        if id == prod["_id"]:
            return json.dumps(prod)

    return abort(404)


@app.route("/api/product/most_expensive")
def get_most_expensive():
    pivot = catalog[0]
    for prod in catalog:
        if prod["price"] > pivot["price"]:
            pivot = prod

    return json.dumps(pivot)


app.run(debug=True)
