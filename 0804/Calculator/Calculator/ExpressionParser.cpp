#include "ExpressionParser.h"
#include <stdexcept>


double ExpressionParser::calculate(
    std::wstring expression
)
{

    int index = 0;

    return parseExpression(
        expression,
        index
    );

}




double ExpressionParser::parseExpression(
    std::wstring& exp,
    int& index
)
{

    double value =
        parseTerm(exp, index);



    while (index < exp.length())
    {

        wchar_t op = exp[index];


        if (op == L'+')
        {

            index++;

            value +=
                parseTerm(exp, index);

        }

        else if (op == L'-')
        {

            index++;

            value -=
                parseTerm(exp, index);

        }

        else
            break;

    }


    return value;

}







double ExpressionParser::parseTerm(
    std::wstring& exp,
    int& index
)
{

    double value =
        parseFactor(exp, index);



    while (index < exp.length())
    {

        wchar_t op =
            exp[index];


        if (op == L'*')
        {

            index++;

            value *=
                parseFactor(exp, index);

        }


        else if (op == L'/')
        {

            index++;

            double num =
                parseFactor(exp, index);


            if (num == 0)
                throw std::exception();


            value /= num;

        }

        else
            break;

    }


    return value;

}







double ExpressionParser::parseFactor(
    std::wstring& exp,
    int& index
)
{

    if (exp[index] == L'(')
    {

        index++;

        double value =
            parseExpression(
                exp,
                index
            );


        index++; // )


        return value;

    }



    double number = 0;



    while (
        index < exp.length()
        &&
        ((exp[index] >= '0' &&
            exp[index] <= '9')
            ||
            exp[index] == '.')
        )
    {

        if (exp[index] == '.')
        {

            index++;

            double div = 10;


            while (
                index < exp.length()
                &&
                exp[index] >= '0'
                &&
                exp[index] <= '9'
                )
            {

                number +=
                    (exp[index] - '0')
                    / div;


                div *= 10;

                index++;

            }


            return number;

        }


        number =
            number * 10 +
            (exp[index] - '0');


        index++;

    }


    return number;

}