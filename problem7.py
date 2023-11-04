import random

num=int(input("How many numbers do you want to put in the list? "))
numbers=[]

p=random.sample(range(1,500), num)
numbers.append(p)

print(numbers)
print(p)