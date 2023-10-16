import requests as req
from sb_requests.simple_books_auth import get_token

URL = "https://simple-books-api.glitch.me"
token = get_token()
header = {'Authorization': f"{token}"}


# Metoda get status va returna statusul un string cu serverului
def get_status():
    status_URL = URL + "/status"
    response = req.get(status_URL)
    # print(response.json()["status"])
    return response.json()["status"]


# get_status()
# print(get_status())

# Returns the list of all books

def get_books():
    books_endpoint = URL + "/books"  # construim endpointul
    response = req.get(books_endpoint)
    # print(response.json())
    return response.json()


# get_books()


# Returns the list of fiction books
def get_type_books(book_type):
    books_endpoint_type = URL + f"/books?type={book_type}"  # construim endpointul pt fiction books
    response = req.get(books_endpoint_type)
    # print(response.json())
    return response.json()


# get_type_books("fiction")

# Returns the list of first 2 non-fiction books
def get_limit_type_books(book_type, limit):
    books_endpoint_type = URL + f"/books?type={book_type}&limit={limit}"  # construim endpointul pt fiction books
    response = req.get(books_endpoint_type)
    # print(response.json())
    return response.json()


# get_type_books("non-fiction", 2)
# print(get_limit_type_books("non-fiction", 2))

# Retrieve detailed information about a book

def get_book_info(book_id):
    books_endpoint = URL + f"/books/{book_id}"  # construim endpointul pentru bookid
    response = req.get(books_endpoint)
    return response.json()


# print(get_book_info(3))

def submit_order():
    data = {
        "bookId": 1,
        "customerName": "John"
    }
    order_endpoint = URL + "/orders"
    response = req.post(order_endpoint, headers=header, json=data)
    return response.json()
