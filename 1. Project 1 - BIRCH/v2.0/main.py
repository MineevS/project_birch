import matplotlib.pyplot as plt
# from scilab2py import scilab

'''plt.plot([1, 2, 3, 4, 5])
plt.plot([1, 2, 3, 4, 5], [1/2, 2/2, 3/2, 4/2, 5/2])
plt.ylabel("some numbers")
plt.show()'''


# import sympy, Point and Ellipse
from sympy import Point, Ellipse, pi, cos, sin, S, is_increasing, singularities, Symbol, log
from sympy.abc import x, y
from sympy.plotting import plot
# x = symbols('x')
  
# using Ellipse() 
ellipse = Ellipse(Point(0, 4), 2, 1)

# Plot the ellipse
#print(dir(Ellipse))
#p = ellipse.plot_interval()
#print(p)


# Add axis labels (optional)
#plt.xlabel('X-axis')
#plt.ylabel('Y-axis')

# Set aspect ratio to be equal (so the ellipse appears as a circle if axes have the same unit)
#plt.axis('equal')

# Show the plot
# plt.show()




# using equation()
# ellipse = ellipse.rotate(angle=pi/2, pt=None)
#ellipse = ellipse.subs()
eq1 = ellipse.equation(x, y);

# theta=pi/3

'''
eq1 = ellipse.xreplace({x: x*cos(theta) - y*sin(theta),
                        y: x*sin(theta) + y*cos(theta)})'''

##print(dir(ellipse))

#print()
#print(eq1)

#eq1.rotate(angle=60, pt=None)

import sympy

def eval_eqn(eqn,in_dict):
    subs = {sympy.symbols(key):item for key,item in in_dict.items()}
    ans = sympy.simplify(eqn).evalf(subs = subs)

    return ans

import math

print(True if round(eval_eqn(eq1,{'x': 1, 'y': 1}), 5) <= 0 else False)
print(True if round(eval_eqn(eq1,{'x': 0, 'y': 3}), 5) <= 0 else False)
print(True if round(eval_eqn(eq1,{'x': 0, 'y': 4}), 5) <= 0 else False)
print(True if round(eval_eqn(eq1,{'x': 0, 'y': 5}), 5) <= 0 else False)
print(True if round(eval_eqn(eq1,{'x': 1, 'y': 3}), 5) <= 0 else False)
print(eval_eqn(eq1,{'x': 1, 'y': 3}))
print(True if round(eval_eqn(eq1,{'x': 1.7, 'y': 4}), 5) <= 0 else False)
print(True if round(eval_eqn(eq1,{'x': 1.7, 'y': 5}), 5) <= 0 else False)
print(eval_eqn(eq1,{'x': 1.7, 'y': 5}))


from sympy import var, plot_implicit
var('x y')
plot_implicit(eq1, x_var=(x, -10, 10), y_var=(y, -10, 10)  ,depth = 2)

#plot(x**2, (x, -5, 5),show=False)
  
print(eq1)

theta=pi/6

eq2 = eq1.xreplace({x: x*cos(theta) - y*sin(theta),
                        y: x*sin(theta) + y*cos(theta)})

print(eq2)

#xgrid(color("grey"),-10, 10)

plot_implicit(eq2, x_var=(x, -10, 10), y_var=(y, -10, 10))

'''
s = solve([
        eq.xreplace({x: x*cos(theta) - y*sin(theta),
                        y: x*sin(theta) + y*cos(theta)}) for p in pts], dict=True)[0]

 eq.subs(s)
 '''
#printt()

# print(is_increasing(eq2, S.Reals))

print(type(eq2))
print(dir(eq2))
print(eq2)

#print(eq2.limit('x' , 'xlim'))

print(ellipse.auxiliary_circle())

x = Symbol('x', real=True)
y = Symbol('y', real=False)

# print(singularities(eq2, x))

from sympy.solvers import solve

solve(eq2, [x, y])





#plot_implicit(eq1, x_var=(x, -10, 10), y_var=(y, -10, 10))



