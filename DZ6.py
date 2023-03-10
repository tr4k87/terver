import numpy as np
from scipy import stats
# ЗАДАЧА 1
# Известно, что генеральная совокупность распределена нормально
# со средним квадратическим отклонением, равным 16.
# Найти доверительный интервал для оценки математического ожидания a с надежностью
# 0.95,
# если выборочная средняя M = 80, а объем выборки n = 256
# sig = 4
# a = 0.05
# M = 80
# n = 256
# P1 = M + (a/2) * (sig/np.sqrt(n))
# P2 = M - (a/2) * (sig/np.sqrt(n))
# print(f'Доверительный интервал находится в промежутке от {P2} до {P1}') 

# ЗАДАЧА 2
# В результате 10 независимых измерений некоторой величины X, выполненных с
# одинаковой точностью,
# получены опытные данные:
# 6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1
# Предполагая, что результаты измерений подчинены нормальному закону распределения
# вероятностей,
# оценить истинное значение величины X при помощи доверительного интервала,
# покрывающего это
# значение с доверительной вероятностью 0,95.

n = 10
arr = np.array([6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1])
m = round(np.mean(arr), 2)
D = np.var(arr, ddof = 1)
t = round((stats.t.ppf(0.975, 9)), 2)
P1 = m - t * np.sqrt(D/10)
P2 = m + t * np.sqrt(D/10)
print(f' данный интервал покрывает значение Х с вероятностью 0.95 {P1}, {P2}')