//
// Created by skidr on 20/10/2019.
//

#include "realFunctions.h"
#include "exercicios_1.h"
#include "systemSolver.h"

#include <iomanip>


double firstFunction(double x) {
    return sin(10.0*x) + cos(3.0*x);
}

double diffFirstFunction(double x) {
    return 10.0*cos(10.0*x) - 3.0*sin(3.0*x);
}

void firstExercise(void) {
    /* alinea a)
     * maxima: plot2d(sin(10*x)+cos(3*x), [x,3,6]);
     * resposta: 9
     */

    /* alinea b)
     *
     * if (f(3)*f(6) > 0 -> nº raizes par
     * else -> nº raizes impar
     *
     * f(3)*f(6) < 0; numero impar (check -> 9)
     *
     * para isolarmos as raizes menor e maior usamos bisseçoes:
     *
     * ora, para  3 <= x <= 6 a eq tem 9 soluçoes
     *
     * como podemos ver na spread existem 9 zeros, o zero mais baixo esta no intervalo [3.2 , 3.3]
     *                                              o zero mais alto está no intervalo [5.6 , 5.7]
     *
     */


    /*
     * alinea c)
     */

    cout << "\n\n\t alinea c)\n";

    cout << fixed << setprecision(4) ;

    double a = 3.2;
    double b = 3.3;
    double p = 0.005;

    double m;
    while (abs((b-a)/b) > p) {
        m = (b + a) /2.0f;
        if (firstFunction(a)*firstFunction(m) <= 0.0)
            b = m;
        else
            a = m;
    }

    cout << "min root(bissec): " << (a+b) / 2.0 << endl;

    a = 5.6;
    b = 5.7;

    while (abs((b-a)/b) > p) {
        m = (b + a) /2.0f;
        if (firstFunction(a)*firstFunction(m) <= 0.0)
            b = m;
        else
            a = m;
    }

    cout << "max root(bissec): " << (a+b) / 2.0 << endl;

    // ----

    a = 3.2;
    b = 3.3;

    int count = 0;
    long max_iterations = 1000;
    double rr;
    while (abs(b-a) > p && count < max_iterations)
    {
        rr = (a * firstFunction(b) - b * firstFunction(a)) / (firstFunction(b) - firstFunction(a));
        if (firstFunction(a) * firstFunction(rr) <= 0.0) {
            b = rr;
        }
        else {
            a = rr;
        }
        // cout << a << ", " << rr << ", " << b << ", " << firstFunction(rr) << endl;
        count++;
    }
    cout << "min root(false pos): " << rr << endl;


    a = 5.6;
    b = 5.7;

    count = 0;
    while (abs((b-a)/b) > p && count < max_iterations)
    {
        rr = (a * firstFunction(b) - b * firstFunction(a)) / (firstFunction(b) - firstFunction(a));
        if (firstFunction(a) * firstFunction(rr) <= 0.0) {
            b = rr;
        }
        else {
            a = rr;
        }
        // cout << a << ", " << rr << ", " << b << ", " << firstFunction(rr) << endl;
        count += 1;
    }

    cout << "max root(false pos): " << rr << endl;

    cout << "\n\n\t alinea d)\n";

    count = 0;
    double g = 3.2;
    double xn = g - firstFunction(g)/diffFirstFunction(g);
    while (abs(g - xn) > p) {
        // cout << "g: " << g;
        g = xn;
        // cout << " xn: " << xn << endl;
        xn = g - firstFunction(g)/diffFirstFunction(g);
        count += 1;
    }
    cout << "min root(newton): " << xn << endl;

    count = 0;
    g = 5.6;
    xn = g - firstFunction(g)/diffFirstFunction(g);
    while (abs(g - xn) > p) {
        // cout << "g: " << g;
        g = xn;
        // cout << " xn: " << xn << endl;
        xn = g - firstFunction(g)/diffFirstFunction(g);
        count += 1;
    }
    cout << "min root(newton): " << xn << endl;


    /*
     * alinea e)
     * newton converges faster, takes less iterations
     */
}

double secondFunction(double x) {
    return exp(-x) - x;
}

double secondFunctionG1(double x) {
    return exp(-x);
}

double secondFunctionG2(double x) {
    return -log(x);
}

void secondExercise(void) {
    /*
     * two possible expressions:
     *
     *  exp(-x); -log(x);
     *
     *  we are going to use only the first one
     */
    double p = 0.0000000001;

    long count1 = 0;
    double g = -0.5;
    cout << "guess: " << g << endl;
    while (abs(g - secondFunctionG1(g)) > p) {
        g = secondFunctionG1(g);
        count1 += 1;
    }
    cout << "root: " << setprecision(4) << g << " with " << count1 << " iterations\n";

    long count2 = 0;
    g = 1.1;
    cout << "guess: " << g << endl;
    while (abs(g - secondFunctionG1(g)) > p) {
        g = secondFunctionG1(g);
        count2 += 1;
    }
    cout << "root: " << setprecision(4) << g << " with " << count2 << " iterations\n";

    if (count1 > count2) {
        cout << "second one is faster\n";
    }
    else
        cout << "first one is faster\n";
}

double f1_new(double x, double y) {
    return x + y -3.0;
}
double f1x_new(double x, double y) {
    return 1;
}
double f1y_new(double x, double y) {
    return 1;
}

double f2_new(double x, double y) {
    return x*x+y*y-9.0;
}
double f2x_new(double x, double y) {
    return 2*x;
}
double f2y_new(double x, double y) {
    return 2*y;
}

void thirdExercise(void) {
    sysNewton(f1_new,f2_new,f1x_new,f1y_new,f2x_new,f2y_new,0.005);
}




