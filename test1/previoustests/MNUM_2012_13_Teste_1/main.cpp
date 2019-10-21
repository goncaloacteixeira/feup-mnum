//
// Created by skidr on 21/10/2019.
//

#include <iostream>
#include <iomanip>

using namespace std;

double func(double x) {
    return x*x*x + 2.0*x*x + 10.0*x - 17.0;
}

double diffFunc(double x) {
    return 3.0*x*x + 4.0*x + 10.0;
}

void ex1(void) {
    double iter = -4.0;
    while (iter < 5.0) {
        cout << iter << setw(10);
        cout << func(iter) << endl;
        if (func(iter) * func(iter+0.1) < 0)
            cout << "1 zero here\n";
        iter += 0.1;
    }
}

void ex5(void) {
    cout << setprecision(4) << fixed;
    double xn = 0.0;
    for (int i = 0; i < 3; i++) {
        cout << "x" << to_string(i) << ": ";
        cout << xn << endl;
        xn = xn - func(xn) / diffFunc(xn);
    }
}
// TODO - Exercicio 6
void ex6(void) {
    return;
}


int main(void) {
    cout << "\t--ex 1--\n";
    ex1();
    cout << "\t Se o maior zero está entre 1.2 e 1.3 então tambem está entre -1.4 e 2.6\n";

    cout << "\t--ex 5--\n";
    ex5();
    return 0;
}
