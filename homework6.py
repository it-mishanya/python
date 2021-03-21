a = int(input("Результат 1 дня пробежки: "))
b = int(input("Желаемый результат: "))
c = 1
while a <= b:
    print(str(c) + " день: " + str(a))
    a = a * 1.1
    c = c + 1
print(str(c) + " день: " + str(a))
print("На " + str(c) + " день пробежки вы достигнете результата ")