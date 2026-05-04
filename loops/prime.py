number  = 2
is_prime = True
if number > 1:
    while number > 2:
        if number % 2 == 0:
            is_prime = False
            break
        number = number - 1

if is_prime:
    print("The number is prime.")
else:
    print("The number is not prime.")