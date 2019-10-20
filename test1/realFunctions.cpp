//
// Created by skidr on 20/10/2019.
//

#include "realFunctions.h"


double bissec(double func (double), double a, double b, double p, long* count) {
    double m;
    while (abs(b-a) > p) {
        m = (b + a) /2.0f;
        if (func(a)*func(m) <= 0.0)
            b = m;
        else
            a = m;
        (*count) += 1;

        // cout << a << ", " << m << ", " << b << ", " << func(m) << endl;
    }
    return (b + a) / 2.0f;
}

double falsePosition(double func (double), double a, double b, double p, long* count)
{
    long max_iterations = 1000;
    double rr;
    while (abs(b-a) > p && (*count) < max_iterations)
    {
        rr = (a * func(b) - b * func(a)) / (func(b) - func(a));
        if (func(a) * func(rr) <= 0.0) {
            b = rr;
        }
        else {
            a = rr;
        }
        // cout << a << ", " << rr << ", " << b << ", " << function(rr) << endl;
        (*count) += 1;
    }
    return rr;
}

double newton(double func (double), double diffFunc (double), double g, double p, long* count) {
    double xn = g - func(g)/diffFunc(g);

    while (abs(g - xn) > p) {
        g = xn;
        xn = g - func(g)/diffFunc(g);
        (*count) += 1;
    }
    return xn;
}

double picardPeano(double func(double), double g, double p, long* count) {

    while (abs(g - func(g)) > p) {
        g = func(g);
        (*count) += 1;
    }
    return g;
}
