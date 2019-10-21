//
// Created by skidr on 21/10/2019.
//

#include <iostream>
#include <iomanip>

#include "newtonSystem.h"

using namespace std;

double func(double x) {
    return x*x*x + 2.0*x*x + 10.0*x - 17.0;
}

double diffFunc(double x) {
    return 3.0*x*x + 4.0*x + 10.0;
}

#include <cmath>

double f1(double x, double y) {
    return y - log(x - 1.0);
}

double f1x(double x, double y) {
    return 1.0 /(x - 1.0);
}

double f1y(double x, double y) {
    return 1;
}

double f2(double x, double y) {
    return y*y + (x-3.0)*(x-3.0) - 4.0;
}

double f2x(double x, double y) {
    return 2.0*(x - 3.0);
}

double f2y(double x, double y) {
    return 2.0*y;
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

void ex6(void) {
    cout << setprecision(4) << fixed;

    newtonMethod(f1, f2, f1x, f1y, f2x, f2y);

}


int main(void) {
    cout << "\t--ex 1--\n";
    ex1();
    cout << "\t Se o maior zero está entre 1.2 e 1.3 então tambem está entre -1.4 e 2.6\n";

    cout << "\t--ex 5--\n";
    ex5();

    cout << "\t--ex 6--\n";
    ex6();

    return 0;
}
