# Задача №23. Для работы в классе
# Дан массив, состоящий из целых чисел. Напишите # программу, которая подсчитает количество 
# элементов массива, больших предыдущего (элемента # с предыдущим номером) 
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения # списка или список задан изначально.
#
#listA = [0, -1, 5, 2, 3]
n = 5
listA = []  # создаем пустой список и дополняем его значениями, вводимыми с клавы 
n = int(input("введите число элементов массива: "))  # задаем длину создваемого списка
for i in range(0,n) :
    newN = int(input("введите следующее число: "))
    listA.append(newN)
print(listA)
# для заданного списка формируем список индексов тех элементов, которые удовлетворяют условию
listRes = [i for i in range(0,n) if listA[i-1] < listA[i] ]
print(listRes)
for i in range(0,len(listRes)) :
    print(i,": ",listA[listRes[i]-1],"  < ", listA[listRes[i]])