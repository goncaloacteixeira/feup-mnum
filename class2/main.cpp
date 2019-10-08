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

double bissec(double a, double b, double p)
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



int main()
{
    double sol[2];
    solver(sol);
    double sol_1, sol_2;
    sol_1 = bissec(0.0, 20.0, 0.00000000000001);

    cout << setprecision(20) << "First solution (CHEATING): " << sol[0] << endl;
    cout << setprecision(20) << "First solution (1): " << sol_1 << endl << endl;

    sol_2 = bissec(-20.0, 0.0, 0.00000000000001);

    cout << setprecision(20) << "Second solution (CHEATING): " << sol[1] << endl;
    cout << setprecision(20) << "Second solution (1): " << sol_2 << endl << endl;

    return 0;
}