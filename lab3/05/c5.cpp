#include <iostream>
#include <utility>  
#include <typeinfo> 
int main() {
    std::pair<double, int> x = {3.14159, 42};

    auto y = x;
    std::cout << "auto: " << typeid(y).name() << std::endl;

    typedef std::pair<double, int> my_pair;
    my_pair z = {2.71828, 100};
    std::cout << "typedef: " << typeid(z).name() << std::endl;

    decltype(x) f = {0.0, 0};
    std::cout << "decltype": " << typeid(f).name() << std::endl;

    int cast = static_cast<int>(x.first);
    std::cout << "static_cast: " << truncated_value << std::endl;

    return 0;
}