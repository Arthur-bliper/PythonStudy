def func(a,b,c):
    print(a,b,c)

my_func = func
my_func(1, 2, 3)
func(1, 2, 3)
print(my_func)
print(func)