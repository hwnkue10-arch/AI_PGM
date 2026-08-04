#include <iostream>
using namespace std;

int main() {

    // (1)
    {
        int a = 5, b = 10;
        cout << "(1) " << (a + b / 3 * 3) << endl;
    }

    // (2)
    {
        int a = 5, b = 10;
        cout << "(2) " << (b << 2) << endl;
    }

    // (3)
    {
        int a = 5, b = 10;
        cout << "(3) " << (a != b) << endl;
    }

    // (4)
    {
        int a = 5, b = 10;
        cout << "(4) " << (b % a) << endl;
    }

    // (5)
    {
        int a = 5, b = 10;
        cout << "(5) " << ((a > b) ? a : b) << endl;
    }

    // (6)
    {
        int a = 5;
        cout << "(6) " << sizeof(a) << endl;
    }

    // (7)
    {
        int a = 5, b = 10, c;
        c = a++;
        cout << "(7) c = " << c << ", a = " << a << endl;
    }

    // (8)
    {
        int a = 5, b = 10;
        a += b;
        cout << "(8) a = " << a << endl;
    }

    // (9)
    {
        int a = 5, b = 10;
        cout << "(9) " << (a & b) << endl;
    }

    // (10)
    {
        int a = 5, b = 10, c;
        c = (a + b, a - b);
        cout << "(10) c = " << c << endl;
    }

    return 0;
}