PRODUCT_TYPES = [
    {
        "id": 1,
        "description": "burrito"
    },
    {
        "id": 2,
        "description": "bowls"
    },
    {
        "id": 3,
        "description": "taco"
    },
    {
        "id": 4,
        "description": "chalupa"
    },
    {
        "id": 5,
        "description": "quesadilla"
    }
]


def get_all_product_types():
    return PRODUCT_TYPES


def get_single_product_type(id):
    requested_product_types = None

    for product_type in PRODUCT_TYPES:
        if product_type["id"] == id:
            requested_product = product_type

    return requested_product_types

def create_product_type(product_type):
    # Get the id value of the last product_type in the list
    max_id = PRODUCT_TYPES[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the product_type dictionary
    product_type["id"] = new_id

    # Add the product_type dictionary to the list
    PRODUCT_TYPES.append(product_type)

    # Return the dictionary with `id` property added
    return product_type
