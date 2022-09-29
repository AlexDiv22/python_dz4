# 1. Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$


# a = int(input('Введите небходимою точность для числа π после запятой: '))
# pi_number = 0
# for i in range(1, 1000000):
#     pi_number += 4 * ((-1) ** (i + 1)) / (2 * i - 1)
# print(str(pi_number)[:a + 2])



# 2. Задайте натуральное число N. Напишите программу, которая составит список простых 
# множителей числа N.

# number = int(input("Введите натуральное число: "))
# i = 2 
# list = []

# while i <= number:
#     if number % i == 0:
#         list.append(i)
#         number //= i
#         i = 2
#     else:
#         i += 1
# print(f"Простые множители указаны в списке: {list}")


# 3. Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.

# numbers = [1, 2, 3, 3, 4, 4, 4, 5, 2, 2, 44, 90, 44, 777]
# list = []
# for i in numbers:
#     if numbers.count(i) == 1:
#         list.append(i)
# print(list)



# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


# from random import randint

# k = int(input('Введите натуральную степень: '))
# power = list()
# for i in range(1, k + 2):
#     power.append(randint(1, 100))

# answer = list()
# for i in range(len(power)):
#     if k == 1:
#         answer.append(f'{power[i]}*x')
#     elif k == 0:
#         answer.append(f'{power[i]}')
#     else:
#         answer.append(f'{power[i]}*x^{k}')
#     flag = randint(0, 1)
#     if flag == 1:
#         answer.append('+')
#     elif flag == 0:
#         answer.append('-')
#     k -= 1

# answer.pop(-1)
# answer.append('=0')
# fout = open('output.txt', 'w')
# fout.write(''.join(answer))
# fout.close()
# print(''.join(answer))



# 5. Даны два файла, в каждом из которых находится запись многочлена. Задача - 
# сформировать файл, содержащий сумму многочленов.


import random
def polynomial_1(a=random.randint(1, 100), b=random.randint(0, 100), c=random.randint(0, 100), result='') -> str:
    if b > 0:
        result += '+' + str(b) + '*x'
    if c > 0:
        result += '+' + str(c)
    return f'{a}*x^2' + result

def polynomial_2(a=random.randint(1, 100), b=random.randint(0, 100), c=random.randint(0, 100), result='') -> str:
    if b > 0:
        result += '+' + str(b) + '*x'
    if c > 0:
        result += '+' + str(c)
    return f'{a}*x^2' + result

f = open('file1.txt', 'w')
f.write(polynomial_1())
print(polynomial_1())
f.close()

f = open('file2.txt', 'w')
f.write(polynomial_2())
print(polynomial_2())
f.close()

f = open('file1.txt', 'r')
list_1 = str(f.readline()).split('x')
c1 = b1 = a1 = 0
if len(list_1) == 3:
    c1 = list_1[2][1:]
if len(list_1) >= 2:
    b1 = list_1[1][3:-1]
a1 = list_1[0][:-1]
f.close()

f = open('file2.txt', 'r')
list_2 = str(f.readline()).split('x')
c2 = b2 = a2 = 0
if len(list_2) == 3:
    c2 = list_2[2][1:]
if len(list_2) >= 2:
    b2 = list_2[1][3:-1]
a2 = list_2[0][:-1]
f.close()

f = open('file_amount.txt', 'w')
f.write(polynomial_1(int(a1) + int(a2), int(b1) + int(b2), int(c1) + int(c2)))
print(polynomial_1(int(a1) + int(a2), int(b1) + int(b2), int(c1) + int(c2)))
f.close()