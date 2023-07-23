# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка # содержит число X
import random
n = int(input("задайте длину массива/списка n="))
# список генерим с помощью датчика случайных чисел
A =[]
for i in range(n) :
    A.append(random.randint(-9,10))
print(A)
X = int(input("введите число-образец, ближайшее к которому будем искать, X="))
indBest = 0
distMin = abs(X-A[indBest])
for i in range (1,len(A)) :
    dist = abs(X-A[i])
    if dist < distMin:
        distMin = dist
        indBest = i
print(A[indBest])
#print("ближайшее ",A[indBest],"  имеет индекс ",indBest)
