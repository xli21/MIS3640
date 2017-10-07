#Assignment 1

print("Please enter a positive integer number：")
n = int(input())
if n <= 0:
    print("Please reenter a 'POSITIVE' integer number")
i=2
if n!=1:
    while i!=n:
        if n % i == 0:
            print(i)
            n = n // i
        else:
            i+=1
    print(i)
else:
    print(n)