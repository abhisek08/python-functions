'''
Write a Python program to print the even numbers from a given list.
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8]
'''
def func(a):
    l=[]
    for i in a:
        if i%2==0:
            l.append(i)
    print(l)
func([1, 2, 3, 4, 5, 6, 7, 8, 9])