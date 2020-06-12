'''
Write a Python function to check whether a number is perfect or not.
Example : The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, and 1 + 2 + 3 = 6.
Equivalently, the number 6 is equal to half the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6.
The next perfect number is 28 = 1 + 2 + 4 + 7 + 14.
This is followed by the perfect numbers 496 and 8128.
'''
def func(n):
    s = 0
    for i in range(1,n):

        if n%i==0:
            s=s+i
    if s==n:
        print('perfect number')
    else:
        print('not a perfect number')
func(8138)