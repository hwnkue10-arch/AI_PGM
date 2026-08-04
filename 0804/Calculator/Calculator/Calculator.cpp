#include "Calculator.h"
#include "ExpressionParser.h"



double Calculator::calculate(
    std::wstring expression
)
{

    return ExpressionParser::calculate(
        expression
    );

}