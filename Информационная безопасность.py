# 1 Упражнение
# Вставляешь из задания p, q, c, (k - это количество знаков "... коды стали длиной k знаков" из 1 упражнения)
p = 31
q = 199
c = 2671
k = 4
# Пишешь каждой переменной массива свой трехзначный код, через запятую(3 цифры - 1 буква слова)
# Хотя бы это сделай)))
a = [207, 238, 236, 239, 232, 228, 243]


# 2 Упражнение
# Самостоятельно разбиваешь свое большое число по количеству знаков и убираешь лишние нули в начале числа
# Пример: 312223953446223521130234         По 4 знака - нули слева! : 3122 2395 3446 2235 2113 234
# Через запятую загоняешь в массив
name = [813, 4634, 8043, 9195, 9486, 5901, 9585, 8703]

# Числа из зыкрытого ключа
# 1 число:
g = 8329
# 2 число:
l = 9617




# Эту часть кода лучше не трогай)))
b = ""
op = ""
p1 = p - 1
q1 = q - 1
N = p * q
for gg in range(N + 1):
    if (c * gg % (p1 * q1)) == 1:
        d = gg
for i in a:
    if k == 5:
        if int(i) ** c % N // 1000 == 0:
            h = ("00" + str(int(i) ** int(c) % N))
            b += h
        elif int(i) ** c % N // 10000 == 0:
            h = ("0" + str(int(i) ** int(c) % N))
            b += h
        else:
            b += str(int(i) ** int(c) % N)
    else:
        if int(i) ** c % N // 100 == 0:
            h = ("00" + str(int(i) ** int(c) % N))
            b += h
        elif int(i) ** c % N // 1000 == 0:
            h = ("0" + str(int(i) ** int(c) % N))
            b += h
        else:
            b += str(int(i) ** int(c) % N)
for i in name:
    temp_in = i ** g % l
    temp_out = chr(temp_in + 848)
    op += temp_out
print("Уппажнение 1")
print("d =", d)
print("N =", N)
print("Зашифрованное значение:", b, "\n")
print("2 Упражнение")
print("Просто вставь это слово в ответ:", op)    
    
