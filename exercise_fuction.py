import math
def quadratic(a, b, c):
    x1 = ((-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)) #quadratic fomular for ax^2+bx+c=0
    x2 = ((-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a))
    print(x1, x2)

a = 3 
b = -7
c = 4
quadratic(a, b, c)