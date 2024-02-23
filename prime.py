my_list = [2,3,4,5,6,7]
for i in my_list:
    flag = 0
    for j in range(2,i):
        if i % j == 0:
            flag = 1
    if flag == 0:
        print(i)


my_list = [2, 3, 4, 5, 6, 7]
prime_numbers = [i for i in my_list if all(i % j != 0 for j in range(2, i))]
print(prime_numbers)



my_list = [2, 3, 4, 5, 6, 7]
prime_numbers = list(filter(lambda x: all(x % j != 0 for j in range(2, x)), my_list))
print(prime_numbers)




