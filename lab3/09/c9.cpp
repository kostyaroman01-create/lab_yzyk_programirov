#include <iostream>

void test(int x, int y, int z) {
    bool result = (x == y == z);
    bool r = x == (y == z);
    std::cout << "x=" << x << ", y=" << y << ", z=" << z <<" (x == y == z)= " << r << std::endl;
}

int main() {

    test(1, 1, 0);
    test(1, 1, 1);
    test(5, 5, 1);

    return 0;
}