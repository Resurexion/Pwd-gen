import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "01234567890"
symbols = "[]{}()*;/,._-"

all = lower + upper + numbers +symbols
lenght = 16
password = "".join(random.sample(all,lenght))
print(password)