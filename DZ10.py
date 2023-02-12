import numpy as np
from scipy import stats
# Задача 1. Провести дисперсионный анализ для определения того, есть ли различия среднего
# роста среди взрослых футболистов, хоккеистов и штангистов.
# Даны значения роста в трех группах случайно выбранных спортсменов:
# Футболисты: 173, 175, 180, 178, 177, 185, 183, 182.
# Хоккеисты: 177, 179, 180, 188, 177, 172, 171, 184, 180.
# Штангисты: 172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170.

fb = np.array([173, 175, 180, 178, 177, 185, 183, 182])
hk = np.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
sht = np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])
k = 3
fbl = len(fb)
hkl = len(hk)
shtl = len(sht)
n = fbl + hkl + shtl
fbm = np.mean(fb)
hkm = np.mean(hk)
shtm = np.mean(sht)
total = np.concatenate([fb, hk, sht])
m_total = np.mean(total)
s2 = np.sum((total - m_total)**2)
s_f = np.sum((fbm - m_total)**2) * fbl + np.sum((hkm - m_total)**2) * hkl + np.sum((shtm - m_total)**2) * shtl
s_o = np.sum((fb - fbm)**2) + np.sum((hk - hkm)**2) + np.sum((sht - shtm)**2)
k1 = k - 1
k2 = n - k
d_f = s_f / k1
d_o = s_o / k2
F_n = d_f / d_o
a = 0.05
F_c = stats.f.ppf(1 - a, k1, k2)
print(f'Т.к. наблюдаемое ({round(F_n, 2)}) > критического ({round(F_c, 2)}), приходим к выводу, что средний рост статически значим')

