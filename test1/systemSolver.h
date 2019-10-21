//
// Created by skidr on 21/10/2019.
//

#ifndef TEST1_SYSTEMSOLVER_H
#define TEST1_SYSTEMSOLVER_H

#include <iostream>

using namespace std;

/** @brief Iteration Method for non-linear systems
 *
 * @param g1 x = g1(x,y)
 * @param g2 y = g2(x,y)
 * @param p  precsion
 */
void sysPicard(double g1(double, double), double g2(double, double), double p);

/** @brief Newton Method for non-linear systems
 *
 * @param f1    f1(x,y)
 * @param f2    f2(x,y)
 * @param f1x   df1/x
 * @param f1y   df1/y
 * @param f2x   df2/x
 * @param f2y   df2/y
 * @param p     precision
 */
void sysNewton(double f1(double, double), double f2(double, double),
                double f1x(double, double), double f1y(double, double),
                double f2x(double, double), double f2y(double, double),
                double p);

#endif //TEST1_SYSTEMSOLVER_H
