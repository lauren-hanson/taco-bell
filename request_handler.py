import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from views import *


class HandleRequests(BaseHTTPRequestHandler):
    def parse_url(self, path):
        path_params = path.split("/")
        resource = path_params[1]
        id = None

        try:
            id = int(path_params[2])
        except IndexError:
            pass
        except ValueError:
            pass

        return (resource, id)

    def do_GET(self):
        response = {}

        # Parse the URL and capture the tuple that is returned
        (resource, id) = self.parse_url(self.path)

        if resource == "products":
            if id is not None:
                self._set_headers(200)
                response = get_single_product(id)

            else:
                self._set_headers(200)
                response = get_all_products()

        elif resource == "product_types":
            if id is not None:
                self._set_headers(405)
                response = ""
            else:
                self._set_headers(200)
                response = get_all_product_types()

        else:
            response = []

        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        self._set_headers(201)

        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        response = {"payload": post_body}
        self.wfile.write(json.dumps(response).encode())

    # def do_POST(self):
    #     self._set_headers(201)
    #     content_len = int(self.headers.get('content-length', 0))
    #     post_body = self.rfile.read(content_len)

    #     # Convert JSON string to a Python dictionary
    #     post_body = json.loads(post_body)

    #     # Parse the URL
    #     (resource, id) = self.parse_url(self.path)

    #     # Initialize new response
    #     new_order = None
        # new_location = None
        # new_employee = None

        # Add a new order to the list. Don't worry about
        # the orange squiggle, you'll define the create_order
        # function next.
        # if resource == "orders":
        #     new_order = create_order(post_body)

        # Encode the new order and send in order
        # self.wfile.write(json.dumps(new_order).encode())

    # def do_DELETE(self):
    #     # Set a 204 response code
    #     self._set_headers(204)

    #     # Parse the URL
    #     (resource, id) = self.parse_url(self.path)

    #     # Delete a single order from the list
    #     if resource == "orders":
    #         delete_order(id)

    #     # Encode the new order and send in response
    #     self.wfile.write("".encode())

    def do_PUT(self):
        """Handles PUT requests to the server """
        self.do_POST()

    # def do_PUT(self):
    #     self._set_headers(204)
    #     content_len = int(self.headers.get('content-length', 0))
    #     post_body = self.rfile.read(content_len)
    #     post_body = json.loads(post_body)

    #     # Parse the URL
    #     (resource, id) = self.parse_url(self.path)

    #     # Delete a single animal from the list
    #     # if resource == "orders":
    #     #     update_order(id, post_body)

    # # Encode the new animal and send in response
    #     self.wfile.write("".encode())

    def _set_headers(self, status):
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                         'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                         'X-Requested-With, Content-Type, Accept')
        self.end_headers()


# point of this application.
def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
