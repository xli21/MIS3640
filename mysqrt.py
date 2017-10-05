import math

a = 1
count = 0
def count_a(a):
    while a < 10:        
        def mysqrt(a):
            x = 3
            y = a
            for i in range (1, 10):
                x = (0.5 * (x + y/x));
            
            print(mysqrt(a))
            a = a + 1
            return x
    

# def mysqrt(a):
#     x = 3
#     y = a
#     for i in range(1, 21):
#         x = (0.5 * (x + y/x));
#     return x

# print (mysqrt(2))
# print (math.sqrt(2) - mysqrt(2))