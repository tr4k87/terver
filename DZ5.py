import numpy as np
from scipy import stats
# Задача 1
# Z крите

# Задача 4

a = 0.05
m = np.array([172, 177, 158, 170, 178, 175, 164, 160, 169, 165])
d = np.array([173, 175, 162, 174, 175, 168, 155, 170, 160, 163])
m_m = np.mean(m)
d_m = np.mean(d)
m_v = np.var(m, ddof = 1)
d_v = np.var(d, ddof = 1)
m_l = len(m)
d_l = len(d)
tn = (m_m - d_m)/ np.sqrt(m_v/m_l + d_v/d_l)
t1 = stats.t.ppf(a/2, df = 2 * (m_l - 1))
t2 = stats.t.ppf(1 - a/2, df = 2 * (d_l - 1))
print(f'Наблюдаемое значение = {round(tn, 2)}, критическое значение = {round(t2, 2)}, можно сделать вывод, что гипотеза верна')