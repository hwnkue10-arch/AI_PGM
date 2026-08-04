#include "Button.h"
#include "Resource.h"

HWND Button::hoverButton = NULL;

void Button::draw(
    LPARAM lParam
)
{

    DRAWITEMSTRUCT* dis =
        (DRAWITEMSTRUCT*)lParam;



    int id =
        dis->CtlID;



    COLORREF color;



    // 숫자 버튼
    color = RGB(60, 60, 60);

    if (dis->hwndItem == hoverButton)
    {
        color = RGB(
            90,
            90,
            90
        );
    }



    // 연산자
    if (
        id == BTN_ADD ||
        id == BTN_SUB ||
        id == BTN_MUL ||
        id == BTN_DIV
        )
    {
        color = RGB(255, 150, 40);
    }



    // =
    if (id == BTN_EQUAL)
    {
        color = RGB(40, 120, 255);
    }



    // C
    if (id == BTN_CLEAR)
    {
        color = RGB(220, 50, 50);
    }

    if (dis->hwndItem == hoverButton)
    {
        color =
            RGB(
                GetRValue(color) + 30,
                GetGValue(color) + 30,
                GetBValue(color) + 30
            );
    }

    if (dis->itemState & ODS_SELECTED)
    {
        color = RGB(
            GetRValue(color) / 2,
            GetGValue(color) / 2,
            GetBValue(color) / 2
        );
    }

    HBRUSH brush =
        CreateSolidBrush(color);


    SelectObject(
        dis->hDC,
        brush
    );


    RoundRect(
        dis->hDC,

        dis->rcItem.left + 3,
        dis->rcItem.top + 3,

        dis->rcItem.right - 3,
        dis->rcItem.bottom - 3,

        15,
        15
    );


    DeleteObject(brush);



    wchar_t text[32];


    GetWindowText(
        dis->hwndItem,
        text,
        32
    );



    SetTextColor(
        dis->hDC,
        RGB(255, 255, 255)
    );


    SetBkMode(
        dis->hDC,
        TRANSPARENT
    );

    HFONT font =
        CreateFont(
            26,
            0,
            0,
            0,
            FW_BOLD,
            FALSE,
            FALSE,
            FALSE,
            DEFAULT_CHARSET,
            OUT_DEFAULT_PRECIS,
            CLIP_DEFAULT_PRECIS,
            DEFAULT_QUALITY,
            DEFAULT_PITCH,
            L"Segoe UI"
        );


    SelectObject(
        dis->hDC,
        font
    );



    DrawText(
        dis->hDC,
        text,
        -1,
        &dis->rcItem,
        DT_CENTER |
        DT_VCENTER |
        DT_SINGLELINE
    );

}

void Button::setHover(HWND hwnd)
{
    if (hoverButton != hwnd)
    {
        HWND old = hoverButton;

        hoverButton = hwnd;


        if (old)
            InvalidateRect(
                old,
                NULL,
                TRUE
            );


        if (hoverButton)
            InvalidateRect(
                hoverButton,
                NULL,
                TRUE
            );
    }
}