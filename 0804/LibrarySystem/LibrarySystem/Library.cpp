#include "Library.h"
#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

// 도서 등록
void Library::addBook()
{
    string title;
    string author;
    string publisher;

    cout << "\n=== 도서 등록 ===\n";

    cin.ignore();

    cout << "제목 : ";
    getline(cin, title);

    cout << "저자 : ";
    getline(cin, author);

    cout << "출판사 : ";
    getline(cin, publisher);

    Book book(title, author, publisher);

    books.push_back(book);

    cout << "도서가 등록되었습니다.\n";
}

void Library::saveFile()
{
    ofstream fout("books.txt");

    if (!fout)
    {
        cout << "파일을 열 수 없습니다.\n";
        return;
    }

    for (int i = 0; i < books.size(); i++)
    {
        fout << books[i].saveData() << endl;
    }

    fout.close();

    cout << "파일 저장 완료!\n";
}

void Library::loadFile()
{
    ifstream fin("books.txt");

    if (!fin)
    {
        cout << "저장된 파일이 없습니다.\n";
        return;
    }

    books.clear();

    string line;

    while (getline(fin, line))
    {
        stringstream ss(line);

        string title;
        string author;
        string publisher;
        string borrowedStr;

        getline(ss, title, '|');
        getline(ss, author, '|');
        getline(ss, publisher, '|');
        getline(ss, borrowedStr);

        bool borrowed = (borrowedStr == "1");

        Book book(title, author, publisher, borrowed);

        books.push_back(book);
    }

    fin.close();

    cout << "파일 불러오기 완료!\n";
}

// 전체 목록
void Library::showBooks()
{
    cout << "\n=== 도서 목록 ===\n";

    if (books.empty())
    {
        cout << "등록된 도서가 없습니다.\n";
        return;
    }

    for (int i = 0; i < books.size(); i++)
    {
        cout << "[" << i + 1 << "]\n";
        books[i].printBook();
    }
}

// 검색
void Library::searchBook()
{
    string keyword;

    cout << "\n검색할 제목 : ";

    cin.ignore();

    getline(cin, keyword);

    bool found = false;

    for (int i = 0; i < books.size(); i++)
    {
        if (books[i].getTitle() == keyword)
        {
            books[i].printBook();
            found = true;
        }
    }

    if (!found)
    {
        cout << "검색 결과가 없습니다.\n";
    }
}

void Library::borrowBook()
{
    string title;

    cout << "\n=== 도서 대출 ===\n";

    cin.ignore();

    cout << "대출할 도서 제목 : ";
    getline(cin, title);

    for (int i = 0; i < books.size(); i++)
    {
        if (books[i].getTitle() == title)
        {
            if (books[i].isBorrowed())
            {
                cout << "이미 대출 중인 도서입니다.\n";
            }
            else
            {
                books[i].borrowBook();
                cout << "대출이 완료되었습니다.\n";
            }

            return;
        }
    }

    cout << "해당 도서를 찾을 수 없습니다.\n";
}

void Library::returnBook()
{
    string title;

    cout << "\n=== 도서 반납 ===\n";

    cin.ignore();

    cout << "반납할 도서 제목 : ";
    getline(cin, title);

    for (int i = 0; i < books.size(); i++)
    {
        if (books[i].getTitle() == title)
        {
            if (!books[i].isBorrowed())
            {
                cout << "이미 반납된 도서입니다.\n";
            }
            else
            {
                books[i].returnBook();
                cout << "반납이 완료되었습니다.\n";
            }

            return;
        }
    }

    cout << "해당 도서를 찾을 수 없습니다.\n";
}

void Library::deleteBook()
{
    string title;

    cout << "\n=== 도서 삭제 ===\n";

    cin.ignore();

    cout << "삭제할 도서 제목 : ";
    getline(cin, title);

    for (int i = 0; i < books.size(); i++)
    {
        if (books[i].getTitle() == title)
        {
            books.erase(books.begin() + i);

            cout << "도서가 삭제되었습니다.\n";

            return;
        }
    }

    cout << "해당 도서를 찾을 수 없습니다.\n";
}