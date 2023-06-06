#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
<<<<<<< HEAD
ld = abs(number) % 10
=======
ld = number % 10
>>>>>>> e679deab95bdb38c8802189f896c749d0c432d87

if ld > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, ld))

elif ld == 0:
<<<<<<< HEAD
    print("Last digit of {} is {} and is 0".format(number, ld))
=======
    print("Last digit of {} is 0".format(number, ld))
>>>>>>> e679deab95bdb38c8802189f896c749d0c432d87

else:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, ld))
