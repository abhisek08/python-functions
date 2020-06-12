'''
 Write a Python function that checks whether a passed string is palindrome or not.
Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward
, e.g., madam or nurses run.
'''
def func(a):
    if a[::]==a[::-1]:
        print('palindrome')
    else:
        print('not palindrome')

func('abba')