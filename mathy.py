import sympy as smp
from sympy import *
# Calculus & Python
x, y=smp.symbols('x y')
pi = smp.pi
# lim as x->pi sin(x/2 + sin(x))  ANS = 1
print(smp.limit(smp.sin(x/2 + smp.sin(x)), x, pi))
