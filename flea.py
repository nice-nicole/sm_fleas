import random
n = 20
# initialize a and b at time 0
a = 20
b = 0
for i in range (1, n+1):
    print("-------------------------------")
    print("At time = ", i)
    random_number= random.random()
    print("generated random number = ", random_number)
    print("a/n = ", a/n)
    if(random_number <= a/n):
        a-=1
        b+=1
    else:
        a+=1
        b-=1
    print(a,b)


