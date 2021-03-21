time = int(input("Введите время в секундах и вы узнаете сколько это будет в часах, минутах и секундах: "))
hour = time // 3600
minute = time % 3600 // 60
seconds = time % 3600 % 60

print(str(hour) + ":" + str(minute) + ":" + str(seconds) + ".")
print("До новых встреч, юный программист!")