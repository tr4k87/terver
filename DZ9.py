import numpy as np
from scipy import stats

# ЗАДАЧА 2
# Посчитать коэффициент линейной регрессии при заработной плате (zp), используя
# градиентный спуск (без intercept).

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
alpha = 1e-6
B1 = 0.1
def mse(B1, y=ks, X=zp, n=10):
    return np.sum((B1 * X - y) ** 2) / n
for i in range(1000):
    fp = (1 / 10) * np.sum(2 * (B1 * zp - ks) * zp)
    B1 -= alpha * fp
    if i % 100 == 0:
        print(f'{i}, B1 : {round(B1 , 3)}, mse: {round(mse(B1), 3)}')