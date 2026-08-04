#pragma once

#include <iostream>
#include <string>

using namespace std;

class Book
{
private:
    string title;       // 제목
    string author;      // 저자
    string publisher;   // 출판사
    bool borrowed;      // 대출 여부

public:
    // 생성자
    Book();
    Book(string t, string a, string p);
    Book(string t, string a, string p, bool b);

    // Getter
    string getTitle();
    string getAuthor();
    string getPublisher();
    bool isBorrowed();

    // Setter
    void setTitle(string t);
    void setAuthor(string a);
    void setPublisher(string p);

    // 기능
    void borrowBook();
    void returnBook();

    void printBook();

    string saveData();
};