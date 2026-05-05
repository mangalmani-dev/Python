
#  function for multiple args
def sum_all(*args):
    print(args)
    for i in args:
        print(2*i)
    return sum(args)


print(sum_all(1,2,3))
# print(sum_all(1,2,3,4))
# print(sum_all(1,2,3))