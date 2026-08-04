import json

from book import Book



class Library:


    def __init__(self):

        self.books = []



    # 도서 등록

    def add_book(
        self,
        title,
        author,
        publisher
    ):


        # 중복 확인

        for book in self.books:

            if book.title == title:

                return False



        book = Book(

            title,

            author,

            publisher,

            False

        )


        self.books.append(book)


        return True





    # 전체 도서 반환

    def get_books(self):

        return self.books






    # 검색

    def search_book(
        self,
        keyword
    ):


        result = []


        for book in self.books:


            if keyword.lower() in book.title.lower():


                result.append(book)



        return result






    # 삭제

    def delete_book(
        self,
        title
    ):


        for book in self.books:


            if book.title == title:


                self.books.remove(book)


                return True



        return False






    # 대출

    def borrow_book(
        self,
        title
    ):


        for book in self.books:


            if book.title == title:


                if book.borrowed:


                    return False



                book.borrowed = True


                return True




        return False






    # 반납

    def return_book(
        self,
        title
    ):


        for book in self.books:


            if book.title == title:


                if not book.borrowed:


                    return False



                book.borrowed = False


                return True




        return False






    # 저장

    def save_file(self):


        data = []



        for book in self.books:


            data.append(

                book.to_dict()

            )




        with open(

            "books.json",

            "w",

            encoding="utf-8"

        ) as file:


            json.dump(

                data,

                file,

                ensure_ascii=False,

                indent=4

            )



        return True






    # 불러오기

    def load_file(self):


        try:


            with open(

                "books.json",

                "r",

                encoding="utf-8"

            ) as file:


                data = json.load(file)





            self.books.clear()



            for item in data:


                self.books.append(

                    Book.from_dict(item)

                )



            return True





        except FileNotFoundError:


            return False
