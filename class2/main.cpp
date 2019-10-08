#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

/* 2*x^2 - 5*x -2 = 0
 * -1 -> BATOTA -> formula resolvente
 *  0 -> Isolamento das raizes, repetir para 2 raizes
 *          a < x1* < b
 *  1 -> Usar bissecção sobre [a, b] para calcular X* com precisão "e"
 *      repetir
 *  2 -> Discutir erros absoluto e relativo máximo quando comparados com erro absoluto e erro
 *      relativo das soluções numéricas
 */

void solver(double* sol)
{
    sol[0] = (5.0 + sqrt(5.0*5.0 + 4.0*2.0*2.0)) / (2.0*2.0);
    sol[1] = (5.0 - sqrt(5.0*5.0 + 4.0*2.0*2.0)) / (2.0*2.0);
}


double function(double x)
{
    return 2.0*x*x - 5.0*x - 2.0;
}

double bissec(double &a, double &b, double p)
{
    double m;
    long count = 0;
    while (abs(b - a) > p)
    {
        m = (b + a) / 2.0;
        if (function(a)*function(m) <= 0.0)
            b = m;
        else
            a = m;
        // cout << a << ", " << m << ", " << b << ", " << function(m) << endl;
        count += 1;
    }
    cout << "With precision set to: " << p << " it took " << count << " iterations." << endl << endl;
    return (b + a) / 2.0;
}


double absolutError(double realValue, double aprValue)
{
    return abs(realValue - aprValue);
}

double absolutMaxError(double a, double b)
{
    return abs(a-b)/2;
}

double relativeError(double realValue, double aprValue)
{
    return absolutError(realValue, aprValue) / realValue;
}

double falsePosition(double &a, double &b, double p)
{
    double rr;
    while (abs(b-a) > p)
    {
        rr = (a * function(b) - b * function(a)) / (function(b) - function(a));
        if (function(a) * function(rr) <= 0)
            b = rr;
        else
            a = rr;
    }
}


int main()
{
    double sol[2];
    solver(sol);
    double sol_1, sol_2;
    double a,  b;
    double precision = 0.00000000001;

    a = 0.0;
    b = 10.0;
    sol_1 = bissec(a, b, precision);

    cout << setprecision(20) << "First solution (CHEATING): " << sol[0] << endl;
    cout << setprecision(20) << "First solution (1): " << sol_1 << endl;
    cout << setprecision(10) << "Absolut error: " << absolutError(sol[0], sol_1) << endl;
    cout << setprecision(10) << "Absolut max error: " << absolutMaxError(a, b) << endl << endl;

    a = -10.0;
    b = 0.0;

    sol_2 = bissec(a, b, precision);

    cout << setprecision(20) << "Second solution (CHEATING): " << sol[1] << endl;
    cout << setprecision(20) << "Second solution (1): " << sol_2 << endl << endl;
    cout << setprecision(10) << "Absolut error: " << absolutError(sol[1], sol_2) << endl;
    cout << setprecision(10) << "Absolut max error: " << absolutMaxError(a, b) << endl;

    return 0;
}