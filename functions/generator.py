def  evengenerator(limit):
    for i in range(2,limit+1,2):
        yield i
        
for num in evengenerator(10):
    print(num)
    