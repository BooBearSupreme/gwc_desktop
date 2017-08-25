random_numbers = [29, 68, 69, 30, 20, 91, 62, 28, 36, 67, 40, 71, 71, 82, 71, 84, 96, 34, 40, 92, 57, 56, 86, 63, 88, 79, 48, 22, 12, 74, 86, 54, 94, 19, 73, 25, 23, 72, 74, 56,53, 52, 55, 10, 37, 48, 82, 84, 57, 45, 85, 48, 58, 56, 95, 21, 47, 98, 71, 38, 24, 51, 28, 71, 52, 33, 78, 78, 77, 24,17, 31, 85, 87, 86, 63, 23, 73, 40, 64, 35, 29, 10, 43, 99, 38, 63, 61, 76, 91, 64, 48, 23, 26, 19, 21, 17, 49, 15, 62]


# for i in range(len(random_numbers)):
#     if (random_numbers[i]%3==0):
#         print(random_numbers[i])
# i is just index as in the integer taking up the spot, but [i] refers to teh specific number itself.
# all da numbas dvisible by 3

# def isPrime(x):
#for printing all prime numbers now
# for num in random_numbers:
#     for i in range(2,num:
#         if (ni)
#     if (num % range(2, num - 1) != 0):
#         print(num)
#     #a number that is divisible is not a prime
    # if (num%2==0 or num%3==0 ...)
    # do something
    # for i in range(2, num-1):
        #last random number is dividble by last rand number, so to num-1
        # if num is evenly divisble by the current number, num ot prime. Is prime if
        #if done checking if it is divisible, then we knwo it prime

# print(isPrime)
def checkPrime(num):
    isPrime= True
    #First assume that the number is divisble by something and then checkt to see its not prime.
    # if prove that infinity goes on forever, first assume that its doesn't, and then prove that wrong.
    # DOuble negation therefore means it goes on forever.
    for i in range(2, num):
        if(num%i==0):
            isPrime= False
    if (isPrime== True):
        print(num)
#checkPrime(31)

#chekc all the numbers]
for num in  random_numbers:
    checkPrime(num)
