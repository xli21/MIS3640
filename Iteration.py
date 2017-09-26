#result = 1
#for i in range (10):
 #   result = result * (i + 1)
  #  print('in the {} th iteration, new result = {}'.format(i, result))
#print(result)


# result = 0

# for i in range(2, 1000, 2):
#     result = result + i
# print(result)


# for alex in ['hello', 'world', 'babson','college']:
#     print(alex)

# iteration = 0
# count = 0
# while iteration < 5:
#     # the variable 'letter' in the loop stands for every 
#     # character, including spaces and commas!
#     for letter in "hello, world": 
#         count += 1
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1 


# iteration = 0
# while iteration < 5:
#     count = 0
#     for letter in "hello, world":
#         count += 1
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1 


# iteration = 0
# while iteration < 5:
#     count = 0
#     for letter in "hello, world":
#         count += 1
#         if iteration % 2 == 0:
#             break
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1 



# while True:
#     line = input('> ')
#     if line == 'done':
#         break
#     print(line)

# print('Done!')



mysum = 1
for i in range(5, 11, 2):
    mysum += i
    if mysum == 5:
        break
print(mysum)