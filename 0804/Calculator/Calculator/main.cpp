#include <windows.h>
#include <string>

#include "UI.h"
#include "Calculator.h"
#include "Resource.h"
#include "Button.h"



Calculator calculator;


std::wstring expression = L"";
bool resultDisplayed = false;

HFONT font;




void updateExpression()
{

    SetWindowText(
        UI::getExpression(),
        expression.c_str()
    );

}







LRESULT CALLBACK WindowProc(
    HWND hwnd,
    UINT msg,
    WPARAM wParam,
    LPARAM lParam
)
{


    switch (msg)
    {

    case WM_CTLCOLORBTN:
    {
        HWND button =
            (HWND)lParam;


        int id =
            GetDlgCtrlID(button);


        return (LRESULT)
            UI::getButtonBrush(id);

    }

    case WM_MOUSEMOVE:
    {
        POINT pt;

        pt.x = LOWORD(lParam);
        pt.y = HIWORD(lParam);


        HWND child =
            ChildWindowFromPoint(
                hwnd,
                pt
            );


        if (child)
        {
            Button::setHover(child);
        }


        break;
    }

    case WM_CREATE:
    {

        font =
            CreateFont(
                32,
                0, 0, 0,
                FW_NORMAL,
                FALSE, FALSE, FALSE,

                DEFAULT_CHARSET,

                OUT_DEFAULT_PRECIS,

                CLIP_DEFAULT_PRECIS,

                DEFAULT_QUALITY,

                DEFAULT_PITCH,

                L"Arial"
            );
    



        UI::setFont(font);


        UI::createControls(hwnd);



        return 0;

    }

    case WM_ERASEBKGND:
    {
        HDC hdc =
            (HDC)wParam;


        RECT rect;


        GetClientRect(
            hwnd,
            &rect
        );


        HBRUSH brush =
            CreateSolidBrush(
                RGB(30, 30, 30)
            );


        FillRect(
            hdc,
            &rect,
            brush
        );


        DeleteObject(brush);


        return 1;
    }

    case WM_DRAWITEM:
    {
        Button::draw(lParam);

        return TRUE;
    }


    case WM_COMMAND:
    {

        int id =
            LOWORD(wParam);



        wchar_t result[100];



        switch (id)
        {



            // 숫자
        case BTN_0:
        case BTN_1:
        case BTN_2:
        case BTN_3:
        case BTN_4:
        case BTN_5:
        case BTN_6:
        case BTN_7:
        case BTN_8:
        case BTN_9:
        {

            wchar_t text[5];


            GetWindowText(
                (HWND)lParam,
                text,
                5
            );


            // 결과가 나온 상태에서 숫자를 누르면 새 계산 시작
            if (resultDisplayed)
            {
                expression = L"";
                resultDisplayed = false;
            }


            expression += text;


            updateExpression();


            break;

        }




        case BTN_ADD:
        case BTN_SUB:
        case BTN_MUL:
        case BTN_DIV:
        {

            // 결과가 표시된 상태면 결과값을 식으로 사용
            if (resultDisplayed)
            {

                wchar_t result[100];


                GetWindowText(
                    UI::getDisplay(),
                    result,
                    100
                );


                expression = result;


                resultDisplayed = false;

            }



            if (id == BTN_ADD)
                expression += L"+";


            else if (id == BTN_SUB)
                expression += L"-";


            else if (id == BTN_MUL)
                expression += L"*";


            else if (id == BTN_DIV)
                expression += L"/";



            updateExpression();


            break;

        }




        case BTN_LEFT:
            expression += L"(";
            updateExpression();
            break;


        case BTN_RIGHT:
            expression += L")";
            updateExpression();
            break;




        case BTN_BACK:

            if (expression.length())
            {
                expression.pop_back();

                updateExpression();
            }

            break;





        case BTN_CLEAR:

            expression = L"";

            updateExpression();


            SetWindowText(
                UI::getDisplay(),
                L"0"
            );

            break;





        case BTN_EQUAL:
        {

            double value =
                calculator.calculate(
                    expression
                );


            swprintf_s(
                result,
                100,
                L"%.2f",
                value
            );


            SetWindowText(
                UI::getDisplay(),
                result
            );


            resultDisplayed = true;


            break;

        }





        case BTN_SIGN:

            expression =
                L"-(" +
                expression +
                L")";


            updateExpression();


            break;


        }



        return 0;

    }






    case WM_DESTROY:

        DeleteObject(font);

        PostQuitMessage(0);

        return 0;


    }



    return DefWindowProc(
        hwnd,
        msg,
        wParam,
        lParam
    );

}







int WINAPI WinMain(
    HINSTANCE hInstance,
    HINSTANCE,
    LPSTR,
    int nCmdShow
)
{


    const wchar_t CLASS_NAME[] =
        L"Calculator";



    WNDCLASS wc = {};



    wc.lpfnWndProc =
        WindowProc;


    wc.hInstance =
        hInstance;


    wc.lpszClassName =
        CLASS_NAME;



    RegisterClass(&wc);





    HWND hwnd =
        CreateWindowEx(
            0,

            CLASS_NAME,

            L"C++ Calculator",

            WS_OVERLAPPEDWINDOW,


            300,
            200,


            460,
            600,


            NULL,
            NULL,
            hInstance,
            NULL
        );



    ShowWindow(
        hwnd,
        nCmdShow
    );




    MSG msg = {};



    while (GetMessage(&msg, NULL, 0, 0))
    {

        TranslateMessage(&msg);

        DispatchMessage(&msg);

    }



    return 0;

}