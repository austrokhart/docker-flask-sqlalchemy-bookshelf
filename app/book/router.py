
from flask import Blueprint, request, jsonify

from book.models_service import list_books, create_book, read_book, update_book, delete_book


router = Blueprint("book", __name__)


@router.route("/list/", methods=["GET"])
def list():

    books = list_books()

    return jsonify(books)


@router.route("/", methods=["POST"])
def create():

    title = request.form["title"]

    result = create_book(title)

    return jsonify(result)


@router.route("/<int:id>/", methods=["GET"])
def read(id):

    result = read_book(id)

    return jsonify(result)


@router.route("/<int:id>/", methods=["PUT"])
def update(id):

    title = request.form["title"]

    result = update_book(id, title)

    return jsonify(result)


@router.route("/<int:id>/", methods=["DELETE"])
def delete(id):

    result = delete_book(id)

    return jsonify(result)
