# Определить, сколько уникальных элементов в списке
# быстрый способ через множество
# x = [1, 1, 2, 0, -1, 3, 4, 4]
# x1 = set(x)
# print(len(x1))

# алгоритмически

# x = [1,2,2,3,3,5,1,2,7,8,4]
# x1= []
# for i in x:
#     if i not in x1:
#         x1.append(i)
# print(len(x1))


# дана последовательность чисел и число K. Напишите программу, которая сдвигает последовательность чисел на K элемнетов в зависимости от знака 
# y = int(input('Введите размер последовательности: '))
# x = list()
# for i in range(0,y):
#     x.append(int(input('Введите элемент последовательности: ')))
# x1 = list()
# print(x)
# n = int(input('Введите число для сдвига: '))
# if n < len(x):
#     if n > 0:
#         for i in range(0,len(x)-n-1):
#             x1.append(x[len(x)-n+i])
#         for i in range(len(x)-n-1,len(x)):
#             x1.append(x[i-n])
#         print(x1)
#     elif n < 0:
#         for i in range(0,len(x)+n):
#             x1.append(x[len(x)+n+i-1])
#         for i in range(len(x)+n,len(x)):
#             x1.append(x[abs(len(x)+n-i)])
#         print(x1)
#     else:
#         print(x)
# else:
#     n %= len(x)
#     if n > 0:
#         for i in range(0,len(x)-n):
#             x1.append(x[len(x)-n+i])
#         for i in range(len(x)-n,len(x)):
#             x1.append(x[i-n])
#         print(x1)
#     elif n < 0:
#         for i in range(0,len(x)-n):
#             x1.append(x[len(x)-n+i])
#         for i in range(len(x)-n,len(x)):
#             x1.append(x[i-n])
#         print(x1)
#     else:
#         print(x)

# не долбаёбское решение, как у меня, через срезы

# y = int(input('Введите размер последовательности: '))
# x = list()
# for i in range(0,y):
#     x.append(int(input('Введите элемент последовательности: ')))
# print(x)
# n = int(input('Введите число для сдвига: '))
# if len(x) > n:
#     x1 = x[-n:]+x[:-n]
#     print(x1)
# elif n >= len(x):
#     n %= len(x)
#     x1 = x[-n:]+x[:-n]
#     print(x1)
# else:
#     print(x)

# нормальное алгоритмическое решение 
# x  = [1,2,4,5,6,6]
# k = 5
# for i in range(k):
#     temp = x.pop()
#     x.insert(0,temp)
#     print(x)
# print(x)
# напишите программу для печати всех уникальных значений в словаре
# list1 = [{'V':'S001'}, {'V': 'S002'}, {'V1':'S001'}, {'V1':'S005'}, {'V2': ' S005 '}, {' V ': 'S009'}, {'V3': 'S007'}]
# set1 = set()
# for i in list1:
#     for k,v in i.items():
#         set1.add(v)
# print(set1)

# альтернативный способ
# list1 = [{'V':'S001'}, {'V': 'S002'}, {'V1':'S001'}, {'V1':'S005'}, {'V2': ' S005 '}, {' V ': 'S009'}, {'V3': 'S007'}]
# set1 = set()
# for i in list1:
#     for j in i.values():
#         set1.add(j)
# print(set1)