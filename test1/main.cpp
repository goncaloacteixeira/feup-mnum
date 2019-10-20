#include <iostream>
#include <cmath>
#include <iomanip>


using namespace std;


double func1(double x) {
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
}


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


int main() {
    double a, b, p, g;
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
    cout << " with precision set to: " << setprecision(6) << p << " ; it took " << count << " iterations\n";
}