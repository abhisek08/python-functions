'''
Write a Python function to multiply all the numbers in a list. Go to the editor
Sample List : (8, 2, 3, -1, 7)
Expected Output : -336
'''
def func(a):
    m=1
    for i in a:
        m=m*i
    print(m)
func([8,2,3,-1,7])