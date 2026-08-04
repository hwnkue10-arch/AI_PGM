#include "UI.h"
#include "Resource.h"


HWND UI::hDisplay = NULL;
HWND UI::hExpression = NULL;
HFONT UI::hFont = NULL;

HFONT UI::hDisplayFont = NULL;
HFONT UI::hExpressionFont = NULL;

HBRUSH UI::hNumberBrush = NULL;
HBRUSH UI::hOperatorBrush = NULL;
HBRUSH UI::hEqualBrush = NULL;
HBRUSH UI::hClearBrush = NULL;



void UI::setFont(HFONT font)
{
    hFont = font;
}



HWND UI::getDisplay()
{
    return hDisplay;
}



HWND UI::getExpression()
{
    return hExpression;
}




void UI::createControls(HWND hwnd)
{

    hDisplayFont =
        CreateFont(
            38,
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


    hExpressionFont =
        CreateFont(
            22,
            0,
            0,
            0,
            FW_NORMAL,
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

    hNumberBrush =
        CreateSolidBrush(
            RGB(60, 60, 60)
        );


    hOperatorBrush =
        CreateSolidBrush(
            RGB(255, 150, 40)
        );


    hEqualBrush =
        CreateSolidBrush(
            RGB(40, 120, 255)
        );


    hClearBrush =
        CreateSolidBrush(
            RGB(220, 60, 60)
        );
    hExpression = CreateWindow(
        L"EDIT",
        L"",
        WS_CHILD |
        WS_VISIBLE |
        WS_BORDER |
        ES_RIGHT,

        20,
        20,
        390,
        40,

        hwnd,
        NULL,
        NULL,
        NULL
    );


    SendMessage(
        hExpression,
        WM_SETFONT,
        (WPARAM)hExpressionFont,
        TRUE
    );




    hDisplay = CreateWindow(
        L"EDIT",
        L"0",

        WS_CHILD |
        WS_VISIBLE |
        WS_BORDER |
        ES_RIGHT,

        20,
        65,
        390,
        60,

        hwnd,
        NULL,
        NULL,
        NULL
    );


    SendMessage(
        hDisplay,
        WM_SETFONT,
        (WPARAM)hDisplayFont,
        TRUE
    );





    const wchar_t* buttons[] =
    {
        L"7", L"8", L"9", L"/",
        L"4", L"5", L"6", L"*",
        L"1", L"2", L"3", L"-",
        L"C", L"0", L".", L"+",
        L"BACK", L"=", L"(", L")",
        L"+/-"
    };



    int id = 1;



    for (int row = 0; row < 6; row++)
    {

        for (int col = 0; col < 4; col++)
        {

            if (id > 21)
                break;



            HWND button = CreateWindow(
                L"BUTTON",

                buttons[id - 1],

                WS_CHILD |
                WS_VISIBLE |
                BS_OWNERDRAW,

                20 + col * 95,
                150 + row * 65,

                85,
                55,

                hwnd,

                (HMENU)(INT_PTR)id,

                NULL,

                NULL
            );



            SendMessage(
                button,
                WM_SETFONT,
                (WPARAM)hFont,
                TRUE
            );


            id++;

        }

    }

}
HBRUSH UI::getButtonBrush(int id)
{

    if (id == BTN_EQUAL)
        return hEqualBrush;


    if (id == BTN_CLEAR)
        return hClearBrush;


    if (
        id == BTN_ADD ||
        id == BTN_SUB ||
        id == BTN_MUL ||
        id == BTN_DIV
        )
        return hOperatorBrush;



    return hNumberBrush;

}
void UI::drawButton(
    LPARAM lParam
)
{

    DRAWITEMSTRUCT* dis =
        (DRAWITEMSTRUCT*)lParam;


    int id =
        dis->CtlID;



    HBRUSH brush;



    if (id == BTN_EQUAL)
    {
        brush =
            CreateSolidBrush(
                RGB(50, 120, 255)
            );
    }

    else if (id == BTN_CLEAR)
    {
        brush =
            CreateSolidBrush(
                RGB(220, 60, 60)
            );
    }

    else if (
        id == BTN_ADD ||
        id == BTN_SUB ||
        id == BTN_MUL ||
        id == BTN_DIV
        )
    {
        brush =
            CreateSolidBrush(
                RGB(255, 150, 50)
            );
    }

    else
    {
        brush =
            CreateSolidBrush(
                RGB(70, 70, 70)
            );
    }



    FillRect(
        dis->hDC,
        &dis->rcItem,
        brush
    );


    DeleteObject(brush);



    wchar_t text[20];


    GetWindowText(
        dis->hwndItem,
        text,
        20
    );



    SetBkMode(
        dis->hDC,
        TRANSPARENT
    );


    SetTextColor(
        dis->hDC,
        RGB(255, 255, 255)
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