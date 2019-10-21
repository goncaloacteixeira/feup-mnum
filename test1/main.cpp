#include <iostream>
#include <cmath>
#include <iomanip>

#include "realFunctions.h"
#include "exercicios_1.h"
#include "systemSolver.h"

using namespace std;

/*double func1(double x) {
    return pow(2.0, sqrt(x)) - 10.0*x + 1.0;
}

double g1(double x) {
    return (pow(2.0, sqrt(x)) + 1.0) / 10.0;
}

double diffFunc1(double x) {
    return (log(2.0) * pow(2.0,sqrt(x) - 1)) / sqrt(x) - 10.0;
}


double func2(double x) {
    return x - log(x) - x;
}


double func3(double x) {
    return exp(sin(x))*cos(2.0*x + 1.0);
}


double func4(double x) {
    return (1.0/tan(x)) * sin(3*x) - x - 1.0;
}*/


double g1(double x, double y) {
    return sqrt((x*(y+5.0) - 1.0)/2.0);
}

double g2(double x, double y) {
    return sqrt(x + log(x)/log(10.0));
}

double f1(double x, double y) {
    return 2.0*x*x - x*y -5.0*x + 1.0;
}

double f2(double x, double y) {
    return x + 3.0*log(x) / log(10.0) - y*y;
}

double f1x(double x, double y) {
    return 4.0*x-y-5.0;
}

double f1y(double x, double y) {
    return -x;
}

double f2x(double x, double y) {
    return 3.0 /(log(10) * x) + 1.0;
}

double f2y(double x, double y) {
    return -2.0*y;
}


int main() {
    /*double a, b, p, g;
    long count;

    cout << "*** Métodos intervalares ***\n";
    cout << "a: ";
    cin >> a;
    cout << "b: ";
    cin >> b;
    cout << "precision: ";
    cin >> p;


    count = 0;
    cout << "Result (bissection) : " << setprecision(20) << bissec(func1, a, b, p, &count);
    cout << " with precision set to: " << setprecision(6) << p << " ; it took " << count << " iterations\n";

    count = 0;
    cout << "Result (false position) : " << setprecision(20) << falsePosition(func1, a, b, p, &count);
    cout << " with precision set to: " << setprecision(6) << p << " ; it took " << count << " iterations\n";

    cout << "\n*** Métodos de Guess ***\n";

    cout << "guess: ";
    cin >> g;

    count = 0;
    cout << "Result (Newton) : " << setprecision(20) << newton(func1, diffFunc1, g, p, &count);
    cout << " with precision set to: " << setprecision(6) << p << " ; it took " << count << " iterations\n";

    count = 0;
    cout << "Result (Picard-Peano) : " << setprecision(20) << picardPeano(g1, g, p, &count);
    cout << " with precision set to: " << setprecision(6) << p << " ; it took " << count << " iterations\n";*/


    sysNewton(f1,f2,f1x,f1y,f2x,f2y,0.00001);
    sysPicard(g1,g2,0.00001);
}