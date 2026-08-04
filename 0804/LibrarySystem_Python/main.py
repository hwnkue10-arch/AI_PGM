from library import Library


def show_menu():

    print("\n=============================")
    print("       도서 관리 시스템")
    print("=============================")

    print("1. 도서 등록")
    print("2. 도서 검색")
    print("3. 전체 도서 목록")
    print("4. 도서 대출")
    print("5. 도서 반납")
    print("6. 도서 삭제")
    print("7. 파일 저장")
    print("8. 파일 불러오기")
    print("0. 종료")

    print("=============================")



def main():

    library = Library()

    # 프로그램 시작 시 자동 불러오기
    library.load_file()


    while True:

        show_menu()

        choice = input("메뉴 선택 : ")


        if choice == "1":

            library.add_book()


        elif choice == "2":

            library.search_book()


        elif choice == "3":

            library.show_books()


        elif choice == "4":

            library.borrow_book()


        elif choice == "5":

            library.return_book()


        elif choice == "6":

            library.delete_book()


        elif choice == "7":

            library.save_file()


        elif choice == "8":

            library.load_file()


        elif choice == "0":

            # 종료 전 자동 저장
            library.save_file()

            print("프로그램을 종료합니다.")
            break


        else:

            print("잘못된 메뉴입니다.")



if __name__ == "__main__":

    main()