//
// Created by skidr on 20/10/2019.
//

#ifndef TEST1_REALFUNCTIONS_H
#define TEST1_REALFUNCTIONS_H

#include <iostream>
#include <cmath>

using namespace std;

double bissec(double func (double), double a, double b, double p, long* count);
double falsePosition(double func (double), double a, double b, double p, long* count);
double newton(double func (double), double diffFunc (double), double g, double p, long* count);
double picardPeano(double func(double), double g, double p, long* count);


#endif //TEST1_REALFUNCTIONS_H
