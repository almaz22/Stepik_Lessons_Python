# Логические операции, операции сравнения

# 1_9_6
# Расставьте скобки в выражении
# a and b or not a and not b
# в соответствии с порядком вычисления выражения (приоритетом операций).
# Всего потребуется 5 пар скобок (внешние скобки входят в их число).
a, b = True, False
var = ((a and b) or ((not a) and (not b)))
print(var)

# 1_9_7
# Выполните код в интерпретаторе Python 3 и вставьте в поле ответа результат вычисления.
# Постарайтесь разобраться, почему интерпретатор выдал именно такой ответ.
# Помните, что любые арифметические операции выше по приоритету операций сравнения и логических операторов.
# Ответ на задание проверяется без учёта регистра символов,
# но помните, что в Python логические значения пишутся с большой буквы: True, False.
x = 5
y = 10
print(y > x * x or y >= 2 * x and x < y)

# 1_9_8
# Найдите результат выражения для заданных значений a и b. Учитывайте регистр символов при ответе.
a = True
b = False
print(a and b or not a and not b)