'''
Write a Python function to find the Max of three numbers.
'''
def func(a,b,c):
    if a>b and a>c:
        print(a)
    elif b>a and b>c:
        print(b)
    else:
        print(c)
func(1,2,3)
