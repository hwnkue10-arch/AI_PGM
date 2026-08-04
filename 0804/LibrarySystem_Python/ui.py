import tkinter as tk
from tkinter import ttk, messagebox

from library import Library



class LibraryUI:


    def __init__(self, root):

        self.root = root

        self.library = Library()


        self.root.title(
            "Library Management System"
        )

        self.root.geometry(
            "800x650"
        )

        self.root.resizable(
            False,
            False
        )


        self.create_widgets()


        self.library.load_file()

        self.refresh_list()



    # =========================
    # UI 생성
    # =========================

    def create_widgets(self):


        # -------------------------
        # 입력 영역
        # -------------------------

        input_frame = tk.Frame(
            self.root
        )

        input_frame.pack(
            pady=10
        )



        tk.Label(
            input_frame,
            text="제목"
        ).grid(
            row=0,
            column=0,
            padx=5
        )


        self.title_entry = tk.Entry(
            input_frame,
            width=30
        )

        self.title_entry.grid(
            row=0,
            column=1,
            pady=3
        )



        tk.Label(
            input_frame,
            text="저자"
        ).grid(
            row=1,
            column=0,
            padx=5
        )


        self.author_entry = tk.Entry(
            input_frame,
            width=30
        )

        self.author_entry.grid(
            row=1,
            column=1,
            pady=3
        )



        tk.Label(
            input_frame,
            text="출판사"
        ).grid(
            row=2,
            column=0,
            padx=5
        )


        self.publisher_entry = tk.Entry(
            input_frame,
            width=30
        )

        self.publisher_entry.grid(
            row=2,
            column=1,
            pady=3
        )




        # -------------------------
        # 관리 버튼
        # -------------------------

        button_frame = tk.Frame(
            self.root
        )

        button_frame.pack(
            pady=10
        )



        # 등록 / 삭제

        manage_frame = tk.Frame(
            button_frame
        )

        manage_frame.pack(
            pady=3
        )


        tk.Button(
            manage_frame,
            text="등록",
            width=15,
            command=self.add_book
        ).pack(
            side="left",
            padx=5
        )


        tk.Button(
            manage_frame,
            text="삭제",
            width=15,
            command=self.delete_book
        ).pack(
            side="left",
            padx=5
        )





        # 대출 / 반납

        borrow_frame = tk.Frame(
            button_frame
        )

        borrow_frame.pack(
            pady=3
        )


        tk.Button(
            borrow_frame,
            text="대출",
            width=15,
            command=self.borrow_book
        ).pack(
            side="left",
            padx=5
        )


        tk.Button(
            borrow_frame,
            text="반납",
            width=15,
            command=self.return_book
        ).pack(
            side="left",
            padx=5
        )





        # 저장 / 불러오기

        file_frame = tk.Frame(
            button_frame
        )

        file_frame.pack(
            pady=3
        )


        tk.Button(
            file_frame,
            text="저장",
            width=15,
            command=self.save_file
        ).pack(
            side="left",
            padx=5
        )


        tk.Button(
            file_frame,
            text="불러오기",
            width=15,
            command=self.load_file
        ).pack(
            side="left",
            padx=5
        )






        # -------------------------
        # 검색 영역
        # -------------------------

        search_frame = tk.Frame(
            self.root
        )

        search_frame.pack(
            pady=5
        )



        self.search_entry = tk.Entry(
            search_frame,
            width=35
        )

        self.search_entry.pack(
            side="left",
            padx=5
        )



        tk.Button(
            search_frame,
            text="검색",
            width=10,
            command=self.search_book
        ).pack(
            side="left",
            padx=3
        )


        tk.Button(
            search_frame,
            text="전체보기",
            width=10,
            command=self.refresh_list
        ).pack(
            side="left",
            padx=3
        )






        # -------------------------
        # 도서 목록
        # -------------------------

        columns = (

            "title",
            "author",
            "publisher",
            "status"

        )


        self.tree = ttk.Treeview(

            self.root,

            columns=columns,

            show="headings"

        )


        self.tree.heading(
            "title",
            text="제목"
        )

        self.tree.heading(
            "author",
            text="저자"
        )

        self.tree.heading(
            "publisher",
            text="출판사"
        )

        self.tree.heading(
            "status",
            text="상태"
        )



        self.tree.column(
            "title",
            width=220
        )

        self.tree.column(
            "author",
            width=150
        )

        self.tree.column(
            "publisher",
            width=150
        )

        self.tree.column(
            "status",
            width=100
        )



        self.tree.pack(

            expand=True,

            fill="both",

            padx=20,

            pady=10

        )



        self.tree.bind(

            "<<TreeviewSelect>>",

            self.show_selected

        )



        self.selected_label = tk.Label(

            self.root,

            text="선택된 도서 : 없음"

        )

        self.selected_label.pack()





    # =========================
    # 목록 갱신
    # =========================

    def refresh_list(self):


        for item in self.tree.get_children():

            self.tree.delete(item)



        for index, book in enumerate(
            self.library.get_books()
        ):


            self.tree.insert(

                "",

                "end",

                values=book.get_info(),

                tags=(str(index),)

            )



        self.selected_label.config(

            text="선택된 도서 : 없음"

        )





    # =========================
    # 선택된 Book
    # =========================

    def get_selected_book(self):


        selected = self.tree.selection()



        if not selected:

            return None



        index = int(

            self.tree.item(

                selected[0]

            )["tags"][0]

        )



        return self.library.books[index]






    def show_selected(self,event):


        book = self.get_selected_book()



        if book:


            self.selected_label.config(

                text=f"선택된 도서 : {book.title}"

            )






    # =========================
    # 등록
    # =========================

    def add_book(self):


        title = self.title_entry.get()

        author = self.author_entry.get()

        publisher = self.publisher_entry.get()



        if not title or not author or not publisher:


            messagebox.showwarning(

                "입력 오류",

                "모든 항목을 입력하세요."

            )

            return



        if not self.library.add_book(

            title,

            author,

            publisher

        ):


            messagebox.showwarning(

                "등록",

                "이미 존재하는 도서입니다."

            )

            return



        self.refresh_list()



        self.title_entry.delete(
            0,
            tk.END
        )

        self.author_entry.delete(
            0,
            tk.END
        )

        self.publisher_entry.delete(
            0,
            tk.END
        )





    # =========================
    # 삭제
    # =========================

    def delete_book(self):


        book = self.get_selected_book()



        if book is None:

            messagebox.showwarning(

                "삭제",

                "도서를 선택하세요."

            )

            return



        self.library.books.remove(book)


        self.refresh_list()





    # =========================
    # 검색
    # =========================

    def search_book(self):


        keyword = self.search_entry.get()


        result = self.library.search_book(
            keyword
        )



        for item in self.tree.get_children():

            self.tree.delete(item)



        for book in result:


            index = self.library.books.index(book)


            self.tree.insert(

                "",

                "end",

                values=book.get_info(),

                tags=(str(index),)

            )





    # =========================
    # 대출
    # =========================

    def borrow_book(self):


        book = self.get_selected_book()



        if book and book.borrow():

            pass


        self.refresh_list()





    # =========================
    # 반납
    # =========================

    def return_book(self):


        book = self.get_selected_book()



        if book and book.return_book():

            pass


        self.refresh_list()





    # =========================
    # 저장 / 불러오기
    # =========================

    def save_file(self):

        self.library.save_file()



    def load_file(self):

        self.library.load_file()

        self.refresh_list()