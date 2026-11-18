import random

pw = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

x = int(input("Que tan larga quiere que sea la contraseña? "))

password = ""

for i in range(x):
    password = password + random.choice(pw)

print("Tu contraseña es:", password)
