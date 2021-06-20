# python 3.9


## Работа с листами
justNumbers = [ 4, 1, 13, 0, 6 ]  # присваиваем значения листу
print(justNumbers)  # выведем значения
print(len(justNumbers))  # количество элементов в списке
print(" ")  # пустая строка для вывода
print("сумма элементов списка =")
print(sum(justNumbers))  # сумма элементов

print(sorted(justNumbers))  # сортировка
#[0, 1, 4, 6, 13]
print(sorted(justNumbers, reverse = True)) # сортировка в обратном порядке
#[13, 6, 4, 1, 0]
justNumbers.append(55)  # добавление элемента
print(justNumbers)
#[4, 1, 13, 0, 6, 55]


#Будьте внимательны при изменении листов
#В примере ниже переменная justNumbers и copyNumbers на самом деле указывают на один и тот же объект.
# В результате, при добавлении в copyNumbers очередного элемента этот элемент добавляется и в исходном листе justNumbers

copyNumbers = justNumbers
copyNumbers.append(66)  # добавляем в лист элемент
print(justNumbers)
#[4, 1, 13, 0, 6, 55, 66]
print(copyNumbers)
#[4, 1, 13, 0, 6, 55, 66]

# если проверить id переменных, то увидим что они одинаковые
print(id(justNumbers))
#1371555455232
print(id(copyNumbers))
#1371555455232
justNumbers = [4, 1, 13, 0, 6, 55]

copyNumbers = justNumbers.copy()  # если использовать метод copy, то создаем копию
copyNumbers.append(66)
# если проверить id переменных теперь, то увидим что они разные
print(id(justNumbers))
#1371555597568
print(id(copyNumbers))
#1371555602624
print(justNumbers)
#[4, 1, 13, 0, 6, 55]
print(copyNumbers)
#[4, 1, 13, 0, 6, 55, 66]

#Вывод части листа
sequence = ['Первый', 'Второй', 'Третий', 'Четвертый', 'Пятый']  # создаем лист
print(sequence[2:3])  # выводим только третий элемент, т.к. четвертый не включается
print(sequence[2])  # выводим только третий элемент
print(type(sequence[2:3]))  # выводим тип получившейся переменной - list
print(type(sequence[2]))  # выводим тип получившейся переменной - str
print(sequence[:3])  # выводим до четвертого элемента, не включая его
print(sequence[-1])  # выводим последний элемент
print(sequence[-2:])  # выводим от предпоследнего до последнего элемента
','.join(sequence)  #  преобразование листа в стоку с разделителем ','
print(sequence)
print(','.join(sequence))  # запишет все элементы через запятую в одно строку
print(type(','.join(sequence)))  # видем что переменная стала строкой - str

### List comprehension
# Дана последовательность чисел. Мы хотим оставить только те, что делятся на 5
sequence = range(0, 40, 3)  # берем элементы от 0 до 40 с шагом 3
# решение в лоб
for num in sequence:  # переберяем все элементы списка 0, 3, 6, 9, 12, ....., 36, 39
    if num % 5 == 0:
        print(num)

# если хотим получить отфильтрованный лист, то будет даже так
filteredSequence = []  # создаем пустой список

for num in sequence:  #
    if num % 5 == 0:
        filteredSequence.append(num)

print(filteredSequence)

# с list comprehension получается покороче
print([x for x in sequence if x % 5 == 0])  # тоже самое что и выше но с использыванием list comprehension