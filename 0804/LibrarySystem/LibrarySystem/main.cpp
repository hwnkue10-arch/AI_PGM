#include <iostream>
#include "Library.h"

using namespace std;

int main()
{
    Library library;

    int menu;

    while (true)
    {
        cout << "\n=============================\n";
        cout << "      도서 관리 시스템\n";
        cout << "=============================\n";
        cout << "1. 도서 등록\n";
        cout << "2. 도서 검색\n";
        cout << "3. 전체 도서 목록\n";
        cout << "4. 도서 대출\n";
        cout << "5. 도서 반납\n";
        cout << "6. 도서 삭제\n";
        cout << "7. 파일 저장\n";
        cout << "8. 파일 불러오기\n";
        cout << "0. 종료\n";
        cout << "=============================\n";
        cout << "메뉴 선택 : ";

        cin >> menu;

        switch (menu)
        {
        case 1:
            library.addBook();
            break;

        case 2:
            library.searchBook();
            break;

        case 3:
            library.showBooks();
            break;

        case 4:
            library.borrowBook();
            break;

        case 5:
            library.returnBook();
            break;

        case 6:
            library.deleteBook();
            break;

        case 7:
            library.saveFile();
            break;

        case 8:
            library.loadFile();
            break;

        case 0:
            cout << "프로그램을 종료합니다.\n";
            return 0;

        default:
            cout << "잘못된 입력입니다.\n";
        }
    }
}