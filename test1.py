def name():
    print("Ray")


def test_dict():
    print("----- Dictionary -----")

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

    print(me["fname"] + " " + me["lname"])
    address = me["current_city"]
    print(address["street"] + " " + address["city"])


def younger_person():
    ages = [12, 42, 32, 50, 56, 14, 78, 30, 51, 89, 12, 38, 67, 10]
    pivot = ages[0]
    for num in ages:
        if num < pivot:
            pivot = num
    print(f"The result is: {pivot}")


younger_person()
test_dict()


name()
