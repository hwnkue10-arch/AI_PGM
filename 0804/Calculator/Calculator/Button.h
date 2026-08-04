#pragma once

#include <windows.h>


class Button
{

public:

    static void draw(
        LPARAM lParam
    );


    static void setHover(
        HWND hwnd
    );


private:

    static HWND hoverButton;

};