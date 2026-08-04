class Book:


    def __init__(
        self,
        title,
        author,
        publisher,
        borrowed=False
    ):

        self.title = title
        self.author = author
        self.publisher = publisher
        self.borrowed = borrowed



    # GUI 표시용 도서 정보 반환

    def get_info(self):

        status = (
            "대출중"
            if self.borrowed
            else "대출가능"
        )


        return (

            self.title,

            self.author,

            self.publisher,

            status

        )



    # 대출

    def borrow(self):


        if self.borrowed:

            return False



        self.borrowed = True

        return True





    # 반납

    def return_book(self):


        if not self.borrowed:

            return False



        self.borrowed = False

        return True





    # JSON 저장용 변환

    def to_dict(self):


        return {


            "title":
                self.title,


            "author":
                self.author,


            "publisher":
                self.publisher,


            "borrowed":
                self.borrowed

        }





    # JSON 데이터를 Book 객체로 변환

    @staticmethod

    def from_dict(data):


        return Book(

            data["title"],

            data["author"],

            data["publisher"],

            data["borrowed"]

        )
