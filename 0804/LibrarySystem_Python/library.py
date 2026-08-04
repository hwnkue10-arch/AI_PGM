import json
import csv

from book import Book


class Library:

    def __init__(self):

        self.books = []


    # 도서 등록
    def add_book(self):

        print("\n=== 도서 등록 ===")

        title = input("제목 : ")
        author = input("저자 : ")
        publisher = input("출판사 : ")


        book = Book(
            title,
            author,
            publisher
        )

        self.books.append(book)

        print("도서가 등록되었습니다.")



    # 전체 도서 출력
    def show_books(self):

        print("\n=== 전체 도서 목록 ===")


        if len(self.books) == 0:
            print("등록된 도서가 없습니다.")
            return


        for book in self.books:
            book.show_info()



    # 도서 검색
    def search_book(self):

        keyword = input("\n검색할 제목 : ")

        found = False


        for book in self.books:

            if book.title == keyword:

                book.show_info()
                found = True


        if not found:
            print("검색 결과가 없습니다.")



    # 도서 삭제
    def delete_book(self):

        title = input("\n삭제할 도서 제목 : ")


        for book in self.books:

            if book.title == title:

                self.books.remove(book)

                print("삭제되었습니다.")
                return


        print("해당 도서를 찾을 수 없습니다.")



    # 도서 대출
    def borrow_book(self):

        title = input("\n대출할 도서 제목 : ")


        for book in self.books:

            if book.title == title:

                if book.borrow():

                    print("대출 완료")

                else:

                    print("이미 대출중입니다.")

                return


        print("도서를 찾을 수 없습니다.")



    # 도서 반납
    def return_book(self):

        title = input("\n반납할 도서 제목 : ")


        for book in self.books:

            if book.title == title:


                if book.return_book():

                    print("반납 완료")

                else:

                    print("이미 반납 상태입니다.")

                return


        print("도서를 찾을 수 없습니다.")



    # JSON 저장
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


        print("파일 저장 완료")



    # JSON 불러오기
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


            print("파일 불러오기 완료")


        except FileNotFoundError:

            print("저장된 파일이 없습니다.")