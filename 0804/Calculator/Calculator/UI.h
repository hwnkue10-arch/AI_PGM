#pragma once

#include <windows.h>


class UI
{

public:

    static void createControls(HWND hwnd);

    static HWND getDisplay();

    static HWND getExpression();

    static void setFont(HFONT font);
    static HBRUSH getButtonBrush(int id);
    static void drawButton(
        LPARAM lParam
    );



private:

    static HWND hDisplay;

    static HWND hExpression;

    static HFONT hFont;

    static HFONT hDisplayFont;
    static HFONT hExpressionFont;

    static HBRUSH hNumberBrush;
    static HBRUSH hOperatorBrush;
    static HBRUSH hEqualBrush;
    static HBRUSH hClearBrush;

};