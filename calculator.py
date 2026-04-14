import math

while True:
    expr = input("Введите выражение: ").replace(" ", "")

    if expr.startswith("!"):
        n = int(expr[1:])
        if n < 0:
            print("Ошибка: факториал отрицательного числа не существует")
        else:
            print("Результат:", math.factorial(n))

    elif "**" in expr:
        a, b = expr.split("**")
        print("Результат:", float(a) ** float(b))

    elif "+" in expr:
        a, b = expr.split("+")
        print("Результат:", float(a) + float(b))

    elif "-" in expr:
        a, b = expr.split("-")
        print("Результат:", float(a) - float(b))

    elif "*" in expr:
        a, b = expr.split("*")
        print("Результат:", float(a) * float(b))

    elif "/" in expr:
        a, b = expr.split("/")
        b = float(b)
        if b == 0:
            print("Ошибка: деление на ноль")
        else:
            print("Результат:", float(a) / b)

    else:
        print("Ошибка: неверный формат выражения")

    again = input("Продолжить? (да/нет): ").lower()
    if again != "да":
        break
