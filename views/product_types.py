TYPES = [
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


def get_all_types():
    return TYPES


def get_single_type(id):
    requested_types = None

    for type in TYPES:
        if type["id"] == id:
            requested_product = type

    return requested_types

def create_type(type):

    if "description" in type: 
    # Get the id value of the last type in the list
        max_id = TYPES[-1]["id"]
        # Add 1 to whatever that number is
        new_id = max_id + 1
        # Add an `id` property to the type dictionary
        type["id"] = new_id
        # Add the type dictionary to the list
        TYPES.append(type)
        # Return the dictionary with `id` property added
        return type
    else: 
        return {}
