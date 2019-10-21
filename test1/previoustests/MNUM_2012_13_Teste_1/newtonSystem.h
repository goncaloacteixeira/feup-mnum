//
// Created by skidr on 21/10/2019.
//

#ifndef MNUM_2012_13_TESTE_1_NEWTONSYSTEM_H
#define MNUM_2012_13_TESTE_1_NEWTONSYSTEM_H

#include <iostream>

using namespace std;

double jacobian(double f1x(double, double), double f1y(double, double),
                double f2x(double, double), double f2y(double, double),
                double xn, double yn);

double hn(double f1(double, double), double f1y(double, double),
          double f2(double, double), double f2y(double, double),
          double xn, double yn, double jacobian);

double kn(double f1x(double, double), double f1(double, double),
          double f2x(double, double), double f2(double, double),
          double xn, double yn, double jacobian);

void newtonMethod(double f1(double, double), double f2(double, double),
                  double f1x(double, double), double f1y(double, double),
                  double f2x(double, double), double f2y(double, double));


#endif //MNUM_2012_13_TESTE_1_NEWTONSYSTEM_H
