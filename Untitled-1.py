a = float(input("Введите первое число: "))
op = input("Введите операцию (+, -, *, /): ")
b = float(input("Введите второе число: "))

if op == '+':
    result = a + b
elif op == '-':
    result = a - b
elif op == '*':
    result = a * b
elif op == '/':
    result = a / b
else:
    result = "Неизвестная операция"

print(f"Результат: {result}")