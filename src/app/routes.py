from flask_restful import Resource, reqparse
from app.models import BOOKS, Book

parser = reqparse.RequestParser()
parser.add_argument('title', type=str, required=True, help="Title is required")
parser.add_argument('author', type=str, required=True, help="Author is required")
parser.add_argument('published_year', type=int, required=True, help="Published year is required")
parser.add_argument('isbn', type=str, required=True, help="ISBN is required")
parser.add_argument('genre', type=str)

search_parser = reqparse.RequestParser()
search_parser.add_argument('author', type=str, location='args')  # Specifies query parameters
search_parser.add_argument('published_year', type=int, location='args')
search_parser.add_argument('genre', type=str, location='args')


class BookList(Resource):
    def get(self):
        return [book.to_dict() for book in BOOKS], 200

    def post(self):
        args = parser.parse_args()
        book = Book(args['title'], args['author'], args['published_year'], args['isbn'], args.get('genre'))
        BOOKS.append(book)
        return book.to_dict(), 201

class BookResource(Resource):
    def get(self, isbn):
        for book in BOOKS:
            if book.isbn == isbn:
                return book.to_dict(), 200
        return {'message': 'Book not found'}, 404

    def put(self, isbn):
        args = parser.parse_args()
        for book in BOOKS:
            if book.isbn == isbn:
                book.title = args['title'] or book.title
                book.author = args['author'] or book.author
                book.published_year = args['published_year'] or book.published_year
                book.genre = args.get('genre') or book.genre
                return book.to_dict(), 200
        return {'message': 'Book not found'}, 404

    def delete(self, isbn):
        global BOOKS
        BOOKS = [book for book in BOOKS if book.isbn != isbn]
        return {'message': f'Book with ISBN {isbn} deleted'}, 200

class BookSearch(Resource):
    def get(self):
        args = search_parser.parse_args()
        result = BOOKS
        if args['author']:
            result = [book for book in result if book.author == args['author']]
        if args['published_year']:
            result = [book for book in result if book.published_year == args['published_year']]
        if args['genre']:
            result = [book for book in result if book.genre == args['genre']]
        if args['title']:
            result = [book for book in result if book.title == args['title']]
            return [book.to_dict() for book in result], 200


def initialize_routes(api):
    api.add_resource(BookList, '/books')
    api.add_resource(BookResource, '/books/<string:isbn>')
    api.add_resource(BookSearch, '/books/search')
