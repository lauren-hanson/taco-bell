import random

PRODUCTS = [
    {
        "id": 1,
        "name": "Loco Gordito Supreme",
        "type_id": 1,
        "date_created": "01/11/2023",
        "suggested_price": 9.49
    },
    {
        "id": 2,
        "name": "Crunchwrap Supreme",
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
        "name": "Fiery Doritos Locos Tacos",
        "type_id": 3,
        "date_created": "01/10/2023",
        "suggested_price": 0.49
    },
    {
        "id": 5,
        "name": "Beefy 5-Layer Dip",
        "type_id": 3,
        "date_created": "01/10/2023",
        "suggested_price": 8.49
    },
    {
        "id": 6,
        "name": "Double Decker Supreme Taco",
        "type_id": 3,
        "date_created": "01/10/2023",
        "suggested_price": 7.49
    },
    {
        "id": 7,
        "name": "Jalapeno Popper Quesarito",
        "type_id": 5,
        "date_created": "01/10/2023",
        "suggested_price": 11.49
    }
]

def get_product_id(): 
    """this will generate random item even if a dictionary has been deleted

    Returns:
        random dictionary from the list
    """
    random_product = random.choice(PRODUCTS)
    return random_product['id']
    # return PRODUCTS[-1]["id"]

def get_all_products():
    return PRODUCTS

def get_single_product(id):
    requested_product = None

    for product in PRODUCTS:
        if product["id"] == id:
            requested_product = product

    return requested_product
