# Задача 1
# Из колоды в 52 карты извлекаются случайным образом 4 карты. 
# a) Найти вероятность того, что все карты – крести. 
# б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.

# # a)
# kol = 52
# kres = 13
# max = 4

# def kresti (max ,kres, kol):
#     A = max / kres
#     B = max / kol
#     print(1/(A/B))

# def tuz (max, kol):
#     A = max / kol-max
#     print(1/(1-A))

# kresti(max, kres, kol)
# tuz(max, kol)

# Задача 2
# На входной двери подъезда установлен кодовый замок, 
# содержащий десять кнопок с цифрами от 0 до 9. Код содержит три цифры, которые нужно нажать одновременно. 
# Какова вероятность того, что человек, не знающий код, откроет дверь с первой попытки?

# def factorial(n):
#     f = 1
#     while n > 1:
#         f *= n
#         n -=1
#     return f
# print(1/(factorial(10)/factorial(3)/factorial(7)))

# Задача 3
# В ящике имеется 15 деталей, из которых 9 окрашены. 
# Рабочий случайным образом извлекает 3 детали. 
# Какова вероятность того, что все извлеченные детали окрашены?

# det = 15
# krash = 10
# max = 3

# def factorial(n):
#     f = 1
#     while n > 1:
#         f *= n
#         n -=1
#     return f

# n = factorial(det)/ (factorial(max)*factorial(det-max))
# m = factorial(krash)/(factorial(max)*factorial(krash-max))
# print(f'Вероятность {round(((m/n)*100), 2)} %')

# В лотерее 100 билетов. Из них 2 выигрышных. Какова вероятность того, 
# что 2 приобретенных билета окажутся выигрышными?

bil = 100
win = 2
max = 2

def factorial(n):
    f = 1
    while n > 1:
        f *= n
        n -=1
    return f

n = factorial(bil)/ (factorial(max)*factorial(bil-max))
m = factorial(win)/(factorial(max)*factorial(win-max))
print(f'Вероятность {round(((m/n)*100), 2)} %')