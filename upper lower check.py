'''
Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
Sample String : 'The quick Brow Fox'
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12
'''
def func(a):
    l=0
    u=0
    for i in a:
        if i.isupper():
            u+=1
        elif i.islower():
            l+=1
    print(u,l)

func('The quick Brow Fox')