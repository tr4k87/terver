# Вероятность того, что стрелок попадет в мишень, выстрелив один раз, равна 0.8. 
# Стрелок выстрелил 100 раз. Найдите вероятность того, что стрелок попадет в цель ровно 85 раз.
# p = 0.8
# n = 100
# k = 85
# q=0.2

# def f(n):
#     f = 1
#     while n > 1:
#         f *= n
#         n -=1
#     return f

# C = f(n)/(f(k)*f((n-k)))
# P = C * (p**k) * (q**(n-k))
# print(round(P,3))

# Вероятность того, что лампочка перегорит в течение первого дня эксплуатации, равна 0.0004. 
# В жилом комплексе после ремонта в один день включили 5000 новых лампочек. 
# Какова вероятность, что ни одна из них не перегорит в первый день? Какова вероятность, что перегорят ровно две?
p = 0.0004
n = 5000
k1=0
k2=2
q= 1-p

def f(n):
    f = 1
    while n > 1:
        f *= n
        n -=1
    return f

C1 = f(n)/(f(k1)*f((n-k1)))
P1 = C1 * (p**k1) * (q**(n-k1))
C2 = f(n)/(f(k2)*f((n-k2)))
P2 = C2 * (p**k2) * (q**(n-k2))

print(f'Вероятность того, что не перегорит ни одной лампочки = {round((P1*100),2)}%')
print(f'Вероятность того, что перегорит 2 лампочки = {round((P2*100),2)}%')