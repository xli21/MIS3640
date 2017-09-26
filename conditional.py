#choise = input('Please choose you are using USA or METRIC')

#if choise == 'USA':
    
#weight = input ('Please enter your weight (lb)')
#height = input ('Please enter your height (in)')
#Your_BMI = print(703 * ((weight) / (height) ** 2))

#if Your_BMI <= 18.5:
    #print('Underweight')
#elif Your_BMI > 18.5 and Your_BMI <= 24.9:
   # print('Normal weight')
#elif Your_BMI > 24.9 and Your_BMI < 29.9:
 #   print('Overweight')
#else:
 #   print('Obesity')



#else:
    #print('Please Choose')


#def your_BMI():
    
    bmi = weight / (height ** 2)
    if bmi <= 18.5:
        print('under')
    elif bmi > 18.5 and bmi <= 24.9:
        print('normal')
    elif bmi > 24.9 and bmi <= 29.9:
        print('Over')
    else:
        print('Obesity')

#weight = input('Enter your weight')
#height = input('Enter your height')





def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n-1)

print_n('Hello', 4)








