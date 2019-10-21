//
// Created by skidr on 21/10/2019.
//

#include "systemSolver.h"

void sysPicard(double g1(double, double), double g2(double, double), double p) {

    cout << "\t---Picard---\n";

    double guess1;
    double guess2;

    cout << "guess x: "; cin >> guess1;
    cout << "guess y: "; cin >> guess1;

    double count = 0;

    while (abs(guess1 - g1(guess1, guess2)) > p || abs(guess2 - g2(guess1, guess2)) > p) {
        guess1 = g1(guess1, guess2);
        guess2 = g2(guess1, guess2);
        count++;
    }

    cout << "x: " << guess1 << endl;
    cout << "y: " << guess2 << endl;
    cout << "iterations: " << count << endl;
}

double hn(double (*f1)(double, double), double (*f2)(double, double), double (*f1x)(double, double),
          double (*f1y)(double, double), double (*f2x)(double, double), double (*f2y)(double, double),
          double x, double y) {

    return (f1(x,y)*f2y(x,y) - f2(x,y)*f1y(x,y)) / (f1x(x,y)*f2y(x,y) - f2x(x,y)*f1y(x,y));
}

double kn(double (*f1)(double, double), double (*f2)(double, double), double (*f1x)(double, double),
          double (*f1y)(double, double), double (*f2x)(double, double), double (*f2y)(double, double),
          double x, double y) {

    return (f2(x,y)*f1x(x,y) - f1(x,y)*f2x(x,y)) / (f1x(x,y)*f2y(x,y) - f2x(x,y)*f1y(x,y));
}



void sysNewton(double (*f1)(double, double), double (*f2)(double, double), double (*f1x)(double, double),
               double (*f1y)(double, double), double (*f2x)(double, double), double (*f2y)(double, double),
               double p) {

    cout << "\t---Newton---\n";

    double x;
    double y;

    cout << "guess x: "; cin >> x;
    cout << "guess y: "; cin >> y;

    double count = 0;

    while (abs(hn(f1,f2,f1x,f1y,f2x,f2y,x,y)) > p || abs(kn(f1,f2,f1x,f1y,f2x,f2y,x,y)) > p) {
        x -= hn(f1,f2,f1x,f1y,f2x,f2y,x,y);
        y -= kn(f1,f2,f1x,f1y,f2x,f2y,x,y);
        count++;
    }


    cout << "x: " << x << endl;
    cout << "y: " << y << endl;
    cout << "iterations: " << count << endl;

}


