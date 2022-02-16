from crypt import methods
from flask import Flask, abort, request
from mock_data import catalog
from about_me import me, test
import json
import random
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


@app.route("/api/catalog")
def get_catalog():
    return json.dumps(catalog)


@app.route("/api/catalog", methods=["POST"])
def save_product():
    # get the data from the req (payload)
    # parse that into a dictionary
    product = request.get_json()  # read the payload ad a dictionary
    # validate
    # title and longer than 5 characters
    if not "title" in product or len(product["title"]) < 5:
        return abort(400, "Title is missing and/or too short")

    # there should be a price
    if not "price" in product:
        return abort(400, "Missing price")

    if not isinstance(product["price"], int) and not isinstance(product["price"], float):
        return abort(400, "Price is invalid")

    # the price should be a greater than 0
    if product["price"] <= 0:
        return abort(400, "Price invalid. Price needs to be greater than 0")

    # assign a unique _id
    product["_id"] = random.randint(10000, 50000)
    # save to catalog
    catalog.append(product)
    # return the product
    return json.dumps(product)

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

# get /api/categories
# return a list of strings, representing the UNIQUE categories


@app.route("/api/product/categories")
def get_categories():

    res = []
    for prod in catalog:
        category = prod["category"]

        # if category not exist inside res
        # push category into res
        if not category in res:
            res.append(category)

    return json.dumps(res)


# create an endpoint that allow the client (react) to retrieve
# all the products that belongs to and specified category
# the client will then send the category and expect a list of products in return

# URL?

@app.route("/api/catalog/<category>")
def products_by_category(category):

    res = []
    # for loop
    for prod in catalog:
        if prod["category"] == category:
            # print each product title
            res.append(prod)
        # print titles only for product that belong to category

    return json.dumps(res)


##################################################################
######### API Methods For Coupon Codes ###########################
##################################################################

coupons = []


@app.route("/api/coupons")
def get_coupons():
    return json.dumps(coupons)


@app.route("/api/coupons", methods=["POST"])
def save_coupon():
    coupon = request.get_json()
    # validate
    if not "code" in coupon:
        return abort(400, "Invalid code")

    if not "discount" in coupon:
        return abort(400, "Not valid")

    coupon["_id"] = random.randint(500, 900)
    coupons.append(coupon)

    return json.dumps(coupon)


@app.route("/api/coupons/<code>")
def get_coupon_by_code(code):
    for coupon in coupons:
        if coupon["code"] == code:
            return json.dumps(coupon)

    return abort(404)


# {
#code: "qwerty"
# discount: 10%
# }

# get
# save new
# get by code


app.run(debug=True)
