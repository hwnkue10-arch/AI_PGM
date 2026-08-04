#include <iostream>
using namespace std;

int main() {
    int i, a, b, sum = 0;

    cout << "Enter two integers: ";
    cin >> a >> b;

    for (i = a; i <= b; i++) {
        sum += i;
    }
    /* 1. while문
    i = a;

    while (i <= b) {
        sum += i;
        i++;
    }

    2. do while문
        i = a;

    do {
        sum += i;
        i++;
    } while (i <= b);

    3. python 언어
    sum = 0

        for i in range(a, b + 1) :
            sum += i
*/

    cout << "Sum from " << a << " to " << b << " = " << sum;

    return 0;
}