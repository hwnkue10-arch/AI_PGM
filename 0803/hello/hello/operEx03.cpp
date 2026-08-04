#include <iostream>
#include <string>
using namespace std;

int main() {
    string name[3];
    int stdNum[3];

    // 입력
    for (int i = 0; i < 3; i++) {
        cout << "Student " << i + 1 << endl;
        cout << "Enter student number: ";
        cin >> stdNum[i];

        cout << "Enter name: ";
        cin >> name[i];

        cout << endl;
    }

    // 출력
    cout << "===== Student List =====" << endl;

    for (int i = 0; i < 3; i++) {
        cout << "Student Number: " << stdNum[i]
            << ", Name: " << name[i] << endl;
    }

    return 0;
}