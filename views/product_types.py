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
