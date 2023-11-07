#1
a = int(input())
b = int(input())
if a > b:
    print("Наибольшее", a)
else:
    print("Наибольшее", b)

#2
number = int(input("Введите число: "))
if number % 2 == 0:
    print(f"{number} - четное число.")
else:
    print(f"{number} - нечетное число.")

#4
# с помощью f заменил переменную на знач
number = int(input("Введите число: "))
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(f"{number} - не является простым числом.")
            break
    else:
        print(f"{number} - является простым числом.")

#7
number = int(input("Введите число: "))
if number % 7 == 0:
    print(f"{number} кратно 7.")
else:
    print(f"{number} не кратно 7.")

#10
a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print("Yes")