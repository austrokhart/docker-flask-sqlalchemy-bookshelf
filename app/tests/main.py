
import json
import unittest

from app import app
from book.models_service import *


test_client = app.test_client()


class MainTests(unittest.TestCase):

    def test_books_list(self):

        """
            clear the table and create one book
        """

        delete_books()
        book_one = create_book("title one")["book"]

        with test_client.get("/book/list/") as response:

            self.assertEqual(
                json.loads(
                    response.get_data(as_text=True)
                ),
                {
                    "status": "success",
                    "books": [
                        book_one
                    ]
                }
            )

        """ 
            clear the table and create several books
        """

        delete_books()

        book_one = create_book("title one")["book"]
        book_two = create_book("title two")["book"]

        with test_client.get("/book/list/") as response:

            self.assertEqual(
                json.loads(
                    response.get_data(as_text=True)
                ),
                {
                    "status": "success",
                    "books": [
                        book_one,
                        book_two
                    ]
                }
            )

    def test_create_book(self):

        """
            clear the table, create one book and list it
        """

        delete_books()

        with test_client.post(
            "/book/",
            data={
                "title": "title one"
            }
        ) as response:

            result = json.loads(
                response.get_data(as_text=True)
            )

            self.assertEqual(
                result["status"],
                "success"
            )

            self.assertEqual(
                list_books(),
                {
                    "status": "success",
                    "books": [
                        result["book"]
                    ]
                }
            )

        """   
            clear the table, create several books and list them
        """

        delete_books()

        with test_client.post(
            "/book/",
            data={
                "title": "title one"
            }
        ) as response:

            result_one = json.loads(
                response.get_data(as_text=True)
            )

            self.assertEqual(
                result_one["status"],
                "success"
            )

            self.assertEqual(
                list_books(),
                {
                    "status": "success",
                    "books": [
                        result_one["book"]
                    ]
                }
            )

        with test_client.post(
            "/book/",
            data={
                "title": "title two"
            }
        ) as response:

            result_two = json.loads(
                response.get_data(as_text=True)
            )

            self.assertEqual(
                result_two["status"],
                "success"
            )

            self.assertEqual(
                list_books(),
                {
                    "status": "success",
                    "books": [
                        result_one["book"],
                        result_two["book"]
                    ]
                }
            )

    def test_read_book(self):

        """
            clear the table, create one book and read it
        """

        delete_books()

        book = create_book("title one")["book"]

        with test_client.get("/book/{}/".format(book["id"])) as response:

            self.assertEqual(
                json.loads(response.get_data(as_text=True)),
                {
                    "status": "success",
                    "book": book
                }
            )

        """
            clear the table, create several books and read them
        """

        delete_books()

        book_one = create_book("title one")["book"]
        book_two = create_book("title two")["book"]

        with test_client.get("/book/{}/".format(book_one["id"])) as response:

            self.assertEqual(
                json.loads(response.get_data(as_text=True)),
                {
                    "status": "success",
                    "book": book_one
                }
            )

        with test_client.get("/book/{}/".format(book_two["id"])) as response:

            self.assertEqual(
                json.loads(response.get_data(as_text=True)),
                {
                    "status": "success",
                    "book": book_two
                }
            )

    def test_update_book(self):

        """
            clear the table, create one book, update it and read it
        """

        delete_books()

        book = create_book("title one")["book"]

        with test_client.put(
            "/book/{}/".format(book["id"]),
            data={
                "title": "title one updated"
            }
        ) as response:

            self.assertEqual(
                json.loads(
                    response.get_data(as_text=True)
                ),
                {
                    "status": "success",
                    "book": {
                        **book,
                        "title": "title one updated"
                    }
                }
            )

            self.assertEqual(
                read_book(book["id"]),
                {
                    "status": "success",
                    "book": {
                        **book,
                        "title": "title one updated"
                    }
                }
            )

        """
            clear the table, create several books, update them and read them
        """

        delete_books()

        book_one = create_book("title one")["book"]
        book_two = create_book("title two")["book"]

        with test_client.put(
            "/book/{}/".format(book_one["id"]),
            data={
                "title": "title one updated"
            }
        ) as response:

            self.assertEqual(
                json.loads(
                    response.get_data(as_text=True)
                ),
                {
                    "status": "success",
                    "book": {
                        **book_one,
                        "title": "title one updated"
                    }
                }
            )

            self.assertEqual(
                read_book(book_one["id"]),
                {
                    "status": "success",
                    "book": {
                        **book_one,
                        "title": "title one updated"
                    }
                }
            )

        with test_client.put(
            "/book/{}/".format(book_two["id"]),
            data={
                "title": "title two updated"
            }
        ) as response:

            self.assertEqual(
                json.loads(
                    response.get_data(as_text=True)
                ),
                {
                    "status": "success",
                    "book": {
                        **book_two,
                        "title": "title two updated"
                    }
                }
            )

            self.assertEqual(
                read_book(book_two["id"]),
                {
                    "status": "success",
                    "book": {
                        **book_two,
                        "title": "title two updated"
                    }
                }
            )

    def test_delete_book(self):

        """
            clear the table, create one book and read it, remove it and read it again, remove it again
        """

        delete_books()

        book = create_book("title one")["book"]

        self.assertEqual(
            read_book(book["id"]),
            {
                "status": "success",
                "book": book
            }
        )

        with test_client.delete("/book/{}/".format(book["id"])) as response:

            self.assertEqual(
                json.loads(
                    response.get_data(as_text=True)
                ),
                {
                    "status": "success",
                    "book": book
                }
            )

            self.assertEqual(
                read_book(book["id"]),
                {
                    "status": "error"
                }
            )

        with test_client.delete("/book/{}/".format(book["id"])) as response:
            self.assertEqual(
                json.loads(
                    response.get_data(as_text=True)
                ),
                {
                    "status": "error"
                }
            )

        """
            clear the table, create several books and list them, remove one and list them again, remove another one 
            and list them again
        """

        delete_books()

        book_one = create_book("title one")["book"]
        book_two = create_book("title two")["book"]

        self.assertEqual(
            list_books(),
            {
                "status": "success",
                "books": [
                    book_one,
                    book_two
                ]
            }
        )

        with test_client.delete("/book/{}/".format(book_two["id"])) as response:

            self.assertEqual(
                json.loads(
                    response.get_data(as_text=True)
                ),
                {
                    "status": "success",
                    "book": book_two
                }
            )

            self.assertEqual(
                list_books(),
                {
                    "status": "success",
                    "books": [
                        book_one
                    ]
                }
            )

        with test_client.delete("/book/{}/".format(book_one["id"])) as response:

            self.assertEqual(
                json.loads(
                    response.get_data(as_text=True)
                ),
                {
                    "status": "success",
                    "book": book_one
                }
            )

            self.assertEqual(
                list_books(),
                {
                    "status": "success",
                    "books": []
                }
            )


if __name__ == "__main__":
    unittest.main()
