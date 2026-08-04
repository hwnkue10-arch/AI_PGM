class Book:

    def __init__(self, title, author, publisher, borrowed=False):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.borrowed = borrowed


    # 도서 정보 출력
    def show_info(self):

        print("------------------------")
        print("제목 :", self.title)
        print("저자 :", self.author)
        print("출판사 :", self.publisher)

        if self.borrowed:
            print("상태 : 대출중")
        else:
            print("상태 : 대출가능")

        print("------------------------")


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


    # JSON 저장용 데이터 변환
    def to_dict(self):

        return {
            "title": self.title,
            "author": self.author,
            "publisher": self.publisher,
            "borrowed": self.borrowed
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