import random
n = 20

sum =0
for i in range(1, n+1):
    a = 19
    b = 1
    count = 1
    while(a!=20):
        count +=1
        # print("-------------------------------")
        # print("At time = ", i)
        random_number = random.random()
        # print("generated random number = ", random_number)
        # print("a/n = ", a/n)
        if(random_number <= a/n):
            a -= 1
            b += 1
        else:
            a += 1
            b -= 1
        # print("(" ,a ,",", b,")")
    print(i, "iterations")        
    print("count : ", count)

    sum += count
print("average value :" ,sum/20)


