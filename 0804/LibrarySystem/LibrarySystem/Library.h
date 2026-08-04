#pragma once

#include <vector>
#include "Book.h"

using namespace std;

class Library
{
private:
    vector<Book> books;

public:
    void addBook();       // 도서 등록
    void searchBook();    // 도서 검색
    void deleteBook();    // 도서 삭제
    void borrowBook();    // 도서 대출
    void returnBook();    // 도서 반납
    void showBooks();     // 전체 목록 출력

    void saveFile();      // 파일 저장
    void loadFile();      // 파일 불러오기
};