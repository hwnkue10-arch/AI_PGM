#include <iostream> 
using namespace std;

class Rectangle {
public:
	int width, height;

	Rectangle();
	Rectangle(int w, int h);
	Rectangle(int length);
	bool isSquare();
};

Rectangle::Rectangle() {
	width = height = 1;
}

Rectangle::Rectangle(int w, int h) {
	width = w; height = h;
}

Rectangle::Rectangle(int length) {
	width = height = length;
}

bool Rectangle::isSquare() {
	if (width == height) return true;
	else return false;
}
int main() {
	Rectangle rect1;
	Rectangle rect2(2, 3);
	Rectangle rect3(3);

	if (rect1.isSquare()) {
		cout << "rect1 is Square" << endl;
	}
	if (rect2.isSquare()) 
		cout << "rect2 is Square" << endl;
	
	if (rect3.isSquare()) cout << "rect3 is Square" << endl;
}