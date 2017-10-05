import math
def quadratic(a, b, c):
    x1 = ((-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)) #quadratic fomular for ax^2+bx+c=0
    x2 = ((-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a))
    print(x1, x2)

a = 1 
b = -1
c = 1
quadratic(a, b, c)      