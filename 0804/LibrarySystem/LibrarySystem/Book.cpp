#include "Book.h"
#include <sstream>

Book::Book()
{
    title = "";
    author = "";
    publisher = "";
    borrowed = false;
}

Book::Book(string t, string a, string p)
{
    title = t;
    author = a;
    publisher = p;
    borrowed = false;
}

Book::Book(string t, string a, string p, bool b)
{
    title = t;
    author = a;
    publisher = p;
    borrowed = b;
}

string Book::getTitle()
{
    return title;
}

string Book::getAuthor()
{
    return author;
}

string Book::getPublisher()
{
    return publisher;
}

bool Book::isBorrowed()
{
    return borrowed;
}

void Book::setTitle(string t)
{
    title = t;
}

void Book::setAuthor(string a)
{
    author = a;
}

void Book::setPublisher(string p)
{
    publisher = p;
}

void Book::borrowBook()
{
    borrowed = true;
}

void Book::returnBook()
{
    borrowed = false;
}

void Book::printBook()
{
    cout << "----------------------------\n";
    cout << "제목 : " << title << endl;
    cout << "저자 : " << author << endl;
    cout << "출판사 : " << publisher << endl;
    cout << "상태 : ";

    if (borrowed)
        cout << "대출중\n";
    else
        cout << "대출가능\n";

    cout << "----------------------------\n";
}

string Book::saveData()
{
    stringstream ss;

    ss << title << "|"
        << author << "|"
        << publisher << "|"
        << borrowed;

    return ss.str();
}