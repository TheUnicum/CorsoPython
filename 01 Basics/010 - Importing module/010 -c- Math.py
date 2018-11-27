#-*- coding: utf-8 -*-
#!/usr/bin/env python
#
# Copyright 2018 Mattia Benedetti
# All rights reserved.
#
# Author: Mattia Benedetti

"""
    -   IMPORTING MODULES    -

    -          MATH          -
Docs
https://docs.python.org/2/library/math.html

9.2. math — Mathematical functions
math.ceil(x)        Return the ceiling of x as a float, the smallest integer value greater than or equal to x.
math.fabs(x)        Return the absolute value of x.
math.factorial(x)   Return x factorial. Raises ValueError if x is not integral or is negative.
math.floor(x)       Return the floor of x as a float, the largest integer value less than or equal to x.
math.trunc(x)       Return the Real value x truncated to an Integral (usually a long integer). Uses the __trunc__ method.

9.2.2. Power and logarithmic functions¶
math.exp(x)         Return e**x.
math.log10(x)       Return the base-10 logarithm of x. This is usually more accurate than log(x, 10).
math.pow(x, y)      Return x raised to the power y. Exceptional cases follow Annex ‘F’ of the C99 standard as far as possible. In particular, pow(1.0, x) and pow(x, 0.0) always return 1.0, even when x is a zero or a NaN. If both x and y are finite, x is negative, and y is not an integer then pow(x, y) is undefined, and raises ValueError.
math.sqrt(x)        Return the square root of x.

9.2.3. Trigonometric functions¶
math.acos(x)        Return the arc cosine of x, in radians.
math.asin(x)        Return the arc sine of x, in radians.
math.atan(x)        Return the arc tangent of x, in radians.
math.atan2(y, x)    Return atan(y / x), in radians. The result is between -pi and pi. The vector in the plane from the origin to point (x, y) makes this angle with the positive X axis. The point of atan2() is that the signs of both inputs are known to it, so it can compute the correct quadrant for the angle. For example, atan(1) and atan2(1, 1) are both pi/4, but atan2(-1, -1) is -3*pi/4.
math.cos(x)         Return the cosine of x radians.
math.hypot(x, y)    Return the Euclidean norm, sqrt(x*x + y*y). This is the length of the vector from the origin to point (x, y).
math.sin(x)         Return the sine of x radians.
math.tan(x)         Return the tangent of x radians.

9.2.4. Angular conversion¶
math.degrees(x)     Convert angle x from radians to degrees.
math.radians(x)     Convert angle x from degrees to radians.

9.2.7. Constants
math.pi             The mathematical constant π = 3.141592…, to available precision.
math.e              The mathematical constant e = 2.718281…, to available precision.

"""


import math

print '9.2. math — Mathematical functions'
print 'ceil(5.6)        :', math.ceil(5.6)
print 'floor(5.6)       :', math.floor(5.6)
print 'factorial(4)     :', math.factorial(4)

print
print '9.2.3. Trigonometric functions'
print 'math.cos(math.pi):', math.cos(math.pi)

print
print '9.2.7. Constants'
print 'math.pi          :',math.pi
print 'math.e           :',math.e
