per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.20, 'СБЕР': 4.0,}
print(per_cent)
money = float(input(("Введите сумму депозита:")))
deposit = [money/100*i for i in per_cent.values()]
for per_cent in range(1):
    print (("CКБ"),"|",(str(max(deposit))))
