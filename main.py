import random
symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
#size = int(input("Сколько символов вы хотите в вашем пороле?"))
while True:
    size = int(input("Введите число!"))
    password = ""
    for i in range(size):
        password += random.choice(symbols)
    print(password)














