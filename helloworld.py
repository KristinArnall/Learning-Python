
#prints numbers between 1-10
# for i in range(1,11):
#     print(i)

#prints every 5 numbers between 1-100
# for i in range(1,101):
#     if i % 5 == 0:
#         print(i)

#fizzbuzz
# for i in range(1,101):
#     if (i % 3 == 0) and (i % 5 == 0):
#         print(i,"fizzbuzz")
#     elif i % 3 == 0:
#         print(i, "fizz") 
#     elif i % 5 == 0:
#         print(i, "buzz")

#prints prime numbers between 1-1000
for i in range(1,1000):
    if i == 1 or i == 2:
        print(i)
        continue

    prime = True
    j = 2

    while prime:
        if i % j == 0: 
            prime = False
        if j > int(i/2):
            break
        else:
            j += 1

    if prime:
        print(i)

