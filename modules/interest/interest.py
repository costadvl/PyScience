"""
Module for computing with interest rates.
Ymbold: A is present amount, A0 in initial amount,
n counts days, and p is the interest rate per year.

Give three of these paramethers, the forth can be 
computed as follows:

    A   = present_amount(A0,p,n)
    A0  = initial_amount(A,p,n)
    n   = days(A0,A,p)
    p   = annual_rate(A0,A,n)
"""

from math import log as ln
import sys


def present_amount(A0, p, n):
    return A0 * (1 + p / (360.0 * 100)) ** n


def initial_amount(A, p, n):
    return A * (1 + p / (360.0 * 100)) ** (-n)


def days(A0, A, p):
    return ln(A / A0) / ln(1 + p / (360.0 * 100))


def annual_rate(A0, A, n):
    return 360 * 100 * ((A / A0) ** (1.0 / n) - 1)


def _verify():
    # compatible values
    A = 2.21339
    A0 = 2.0
    p = 5
    n = 730
    # given three of these, compute the remaining value
    A_computed = present_amount(A0, p, n)
    A0_computed = initial_amount(A, p, n)
    n_computed = days(A0, A, p)
    p_computed = annual_rate(A0, A, n)
    print('A=%g (%g)\nA0=%g (%.1f)\nn=%d (%d)\np=%g (%.1f)' %
          (A_computed, A, A0_computed, A0,
           n_computed, n, p_computed, p))

def _compute_missing_parameter(init_code):
    try:
        exec(init_code)
    except SyntaxError as e:
        print(e)
        print(init_code)
        sys.exit(1)
    #find missing parameter
    try:
        if 'A=' not in init_code:
            print('A=',present_amount(A0,p,n))
        elif 'A0=' not in init_code:
            print('A0=', initial_amount(A,p,n))
        elif 'n=' not in init_code:
            print('n=', days(A0,A,p))
        elif 'p=' not in init_code:
            print('p=',annual_rate(A0,A,n))
    except NameError as e:
        print('error type')
        print(e)
        sys.exit(1)
    except ValueError as e:
        print('illegal values in input:',init_code)
        sys.exit(1)

_filename = sys.argv[0]
_usage = """
Usage: %s A=10 p=5 n=730
Program computes and prints the 4th parameter'
(A, A0, p, or n)""" % _filename

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print(_usage)
    elif len(sys.argv) == 2 and sys.argv[1] == 'verify':
        _verify()
    else:
        init_code = ''
        for statement in sys.argv[1:]:
            init_code += statement + '\n'
        exec(init_code)
        _compute_missing_parameter(init_code)

