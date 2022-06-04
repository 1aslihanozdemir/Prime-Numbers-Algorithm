num = int(input("number: "))

prime_numbers = []
prime_numbers.append(2)

for i in range(3,num+1):

    Is_Prime = False
    for j in range(2,i):
        if i%j==0:
            Is_Prime = False
            break
        else :
            Is_Prime = True
    if Is_Prime == True:
        prime_numbers.append(i)


print(prime_numbers)
