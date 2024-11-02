from random import randint

# generate random numbers
otp = randint(156780, 423456)
print(otp)


import os

path = os.getcwd()
print(path)
os.mkdir(f"{path}\\folder")
