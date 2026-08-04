#include <iostream>
using namespace std;

class Circle {
public :
		int radius;
	double getArea();
};

double Circle::getArea() {
	return 3.141592 * radius * radius;
}

int main() {
	Circle dount;
	dount.radius = 1;
	double area = dount.getArea();
	cout << "Donut area = " << area << endl;
	Circle pizza;
	pizza.radius = 30;
	area = pizza.getArea();
	cout << "Pizza area = " << area;
}