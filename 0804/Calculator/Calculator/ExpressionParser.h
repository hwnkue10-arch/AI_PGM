#pragma once

#include <string>


class ExpressionParser
{

public:

    static double calculate(
        std::wstring expression
    );


private:

    static double parseExpression(
        std::wstring& exp,
        int& index
    );


    static double parseTerm(
        std::wstring& exp,
        int& index
    );


    static double parseFactor(
        std::wstring& exp,
        int& index
    );

};