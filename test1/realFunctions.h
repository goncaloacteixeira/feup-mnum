//
// Created by skidr on 20/10/2019.
//

#ifndef TEST1_REALFUNCTIONS_H
#define TEST1_REALFUNCTIONS_H

#include <iostream>
#include <cmath>

using namespace std;


/** @brief Bisection Method to approximate root within a range "a" to "b"
 *
 * This method is reliable but slowly converges to the approx value
 *
 * @param func      function to approximate roots
 * @param a         lower bound
 * @param b         higher bound
 * @param p         precision
 * @param count     counts the number of iterations
 * @return          the approximate value of the root
 */
double bissec(double func (double), double a, double b, double p, long* count);

/** @brief False-Position Method to approximate root within a range "a" to "b"
 *
 * This method is faster than the Bisection Method
 *
 * @param func      function to approximate roots
 * @param a         lower bound
 * @param b         higher bound
 * @param p         precision
 * @param count     counts the number of iterations
 * @return          the approximate value of the root
 */
double falsePosition(double func (double), double a, double b, double p, long* count);

/** @brief Newton Method to approximate root starting with a guess "g"
 *
 * @param func          function to approximate roots
 * @param diffFunc      differential function of @param func
 * @param g             initial guess
 * @param p             precision
 * @param count         counts the number of iterations
 * @return              the approximate value of the root
 */
double newton(double func (double), double diffFunc (double), double g, double p, long* count);

/** @brief Picard-Peano Method to approximate root starting with a guess "g"
 *
 * @param func          function g(x)=0 as x = g(x)
 * @param g             initial guess
 * @param p             precision
 * @param count         counts the number of iterations
 * @return              the approximate value of the root
 */
double picardPeano(double func(double), double g, double p, long* count);


#endif //TEST1_REALFUNCTIONS_H
