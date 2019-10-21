//
// Created by skidr on 21/10/2019.
//

#include "newtonSystem.h"

double jacobian(double f1x(double, double), double f1y(double, double),
                double f2x(double, double), double f2y(double, double),
                double xn, double yn) {

    return f1x(xn, yn) * f2y(xn, yn) - f2x(xn, yn)*f1y(xn, yn);
}

double hn(double f1(double, double), double f1y(double, double),
          double f2(double, double), double f2y(double, double),
          double xn, double yn, double jacobian) {

    return - (f1(xn, yn) * f2y(xn, yn) - f2(xn, yn) * f1y(xn, yn)) / jacobian;
}

double kn(double f1x(double, double), double f1(double, double),
          double f2x(double, double), double f2(double, double),
          double xn, double yn, double jacobian) {

    return - (f1x(xn, yn) * f2(xn, yn) - f2x(xn, yn) * f1(xn, yn)) / jacobian;
}

void newtonMethod(double f1(double, double), double f2(double, double),
                    double f1x(double, double), double f1y(double, double),
                    double f2x(double, double), double f2y(double, double)) {

    double xn, yn;
    cout << "X guess: "; cin >> xn;
    cout << "Y guess: "; cin >> yn;

    double j = jacobian(f1x, f1y, f2x, f2y, xn, yn);

    cout << hn(f1, f1y, f2, f2y, xn, yn, j) << endl;
    cout << kn(f1x, f1, f2x, f2, xn, yn, j) << endl;

    int i = 0;

    while ( (abs(hn(f1, f1y, f2, f2y, xn, yn, j)) >= 0.00001 || abs(kn(f1x, f1, f2x, f2, xn, yn, j)) >= 0.00001 ) && i != 2) {
        xn += hn(f1, f1y, f2, f2y, xn, yn, j);
        yn += kn(f1x, f1, f2x, f2, xn, yn, j);

        j = jacobian(f1x, f1y, f2x, f2y, xn, yn);

        cout << "xn: " << xn << endl;
        cout << "yn: " << yn << endl << endl;
        i++;
    }
}
