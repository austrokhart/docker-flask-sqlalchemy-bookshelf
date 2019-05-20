
from database import session
from book.models import Book
from helpers import entity_to_dict


def create_book(title):

    try:

        book = Book(title=title)

        session.add(book)
        session.commit()

        result = {
            "status": "success",
            "book": entity_to_dict(book)
        }

    except:

        session.rollback()

        result = {
            "status": "error"
        }

    return result


def read_book(id):

    try:

        book = Book.query.filter_by(id=id).first()

        if book:

            result = {
                "status": "success",
                "book": entity_to_dict(book)
            }

        else:

            result = {
                "status": "error"
            }

    except:

        session.rollback()

        result = {
            "status": "error"
        }

    return result


def update_book(id, title):

    try:

        book = Book.query.filter_by(id=id).first()

        if book:

            book.title = title

            session.commit()

            result = {
                "status": "success",
                "book": entity_to_dict(book)
            }

        else:

            result = {
                "status": "error"
            }

    except:

        session.rollback()

        result = {
            "status": "error"
        }

    return result


def delete_book(id):

    try:

        book = Book.query.filter_by(id=id).first()

        if book:

            session.delete(book)
            session.commit()

            result = {
                "status": "success",
                "book": entity_to_dict(book)
            }

        else:

            result = {
                "status": "error"
            }

    except:

        session.rollback()

        result = {
            "status": "error"
        }

    return result


def list_books():

    try:

        books = Book.query.all()

        result = {
            "status": "success",
            "books": [entity_to_dict(book) for book in books]
        }

    except:

        session.rollback()

        result = {
            "status": "error"
        }

    return result


def delete_books():

    try:

        Book.query.delete()

        result = {
            "status": "success"
        }

    except:

        result = {
            "status": "error"
        }

    return result
