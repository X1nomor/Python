import math
import random

# a = float(input())
# b = float(input())
# c = input()
# if c == '+':
#     return
# if c == '-':
#     return a - b
# if c ==
# a = int(input()) Задание 5
# b = 1
# for i in range(1, a+1):
#     b *= i
# print(b)
# a = int(input()) Задание 4
# b = int(input())
# c = int(input())
# for i in range(a, b, c):
#     print(i)
a = random.randint(0, 10)
b = int(input())
c = 1
if b != a:
    while c <= 10:
        if a > b:
            print("Введите число больше")
            b = int(input())
        elif a < b:
            print("No")
            b = int(input())
        else:
            print("You win")
            break