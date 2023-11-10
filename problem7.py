import random

num=int(input("How many numbers do you want to put in the list? "))

p=random.sample(range(1,100), num)
for i in p:
    p.append(i)
    if i==i:
        p.remove(i)


print(p)
