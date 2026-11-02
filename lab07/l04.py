def apply(lst: list, f):
    new_lst=[]
    for el in lst:
        new_lst.append(f(el))
    print(new_lst)

def func1(x):
    return x**2

def func2(x):
    return x**0.5

func3 = lambda x: x**2

apply([1,2,3,4],func1)
apply([1,2,3,4],func2)
apply([1,2,3,4],lambda x: x**3)
