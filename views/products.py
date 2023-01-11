PRODUCTS = [
    {
        "id": 1,
        "name": "Loco Gordito Supreme",
        "type_id": 1,
        "date_created": "01/11/2023",
        "suggested_price": 8.49
    },
    {
        "id": 2,
        "name": "Crunch Wrap Supreme",
        "type_id": 1,
        "date_created": "01/11/2023",
        "suggested_price": 5.49
    },
    {
        "id": 3,
        "name": "Bean Crunch Bowl",
        "type_id": 2,
        "date_created": "01/11/2023",
        "suggested_price": 3.49
    },
    {
        "id": 4,
        "name": "Bean Crunch Bowl",
        "type_id": 2,
        "date_created": "01/10/2023",
        "suggested_price": 0.49
    }
]


def get_all_products():
    return PRODUCTS

# Function with a single parameter


def get_single_product(id):
    # Variable to hold the found product, if it exists
    requested_product = None

    # Iterate the PRODUCTS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for product in PRODUCTS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if product["id"] == id:
            requested_product = product

    return requested_product
