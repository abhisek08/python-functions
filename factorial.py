'''
Write a Python function to calculate the factorial of a number (a non-negative integer).
The function accepts the number as an argument.
'''
def func(n):
    m=1
    for i in range(1,n+1):
        m=m*i
    print(m)
func(5)

