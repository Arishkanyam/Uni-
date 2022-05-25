# -*- coding: utf-8 -*-
"""Copy of КР-ЗБ-ПИ21-*.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rdJpG9g_CMYzG354tVLlFOP29hIYdPkP

#Контрольная работа

# 1.

Напишите **рекурсивную** функцию ```fact```, которая вычисляет факториал заданного числа ```x```.
"""

def fact(x):
    if x <=1:
      return 1
    else:
        return (x* fact(x-1))
x=int(input('Введите число: '))
print('Факториал =', fact(x))

"""#2
 Создайте функцию ```filter_even```, которая принимает на вход список целых чисел,  и фильтруя, возвращает список, содержащий только четные числа. Используйте ```filter``` для фильтрации и  ```lambda```.
"""

def filter_even(li):
  even_li= list(filter(lambda x: x%2==0,li))
  return even_li
li=[1,5,756,34,2,35,76,87,8]
print('Even list:', filter_even(li))

"""#3
Напишите функцию ```square``` ,которая принимает на вход список целых чисел и возвращает список с возведенными в квадрат элементами. Используйте ```map```.
"""

def square(li):
  squares_li = list(map(lambda x: x**2,li))
  return squares_li
li=[1,2,3,4,5,7,8,9,6,10]
print('Квадраты чисел:', square(li))

"""#4
Напишите функцию бинарного поиска ```bin_search```, которая принимает на вход отсортированный список и элемент. Функция должна возвращать индекс искомого элемента в списке. 

Ввод: 
```
[2,5,7,9,11,17,222] 11
```
Вывод: 
 ```
 4
 ```

Ввод:
```
 [2,5,7,9,11,17,222] 12
```
Вывод:
```
  -1
```
"""

def bin_search(li, element):
    low=0
    high=len(li)-1
    mid=0
    while low<=high:
        mid = (high + low)//2
        if li[mid]<element:
            low = mid+1
        elif li[mid]>element:
            high = mid-1
        else: 
            return mid
    return -1

li, element=[2,5,7,9,11,17,222],11
print(bin_search(li,element))
li, element=[2,5,7,9,11,17,222],12
print(bin_search(li,element))

"""#5
Напишите функцию ```is_palindrome``` определяющую,является ли строка палиндромом.
Палиндромами являются текстовые строки, которые одинаково читаются слева направо и справа налево. В строках не учитываются знаки препинания, пробельные символы и цифры; регистр не имеет значения. 

На вход подается строка ```string```.

Выведите YES, если строка является палиндромом и NO иначе.

Запрещается использовать reverse списка - ```list[::-1]``` и функцию ```reversed```.
Чтобы учесть это ограничение, эту задачу рекомендуется решать используя технику решения задач "два указателя". Один указатель читает только символы слева направо, а второй - справа налево.

Примеры:

Ввод 
```
Madam, I'm Adam
``` 
Вывод
```
YES
```
Ввод
```
А роза упала на лапу Азора
``` 
Вывод  
```
YES
```
"""

def is_palindrome(string):
    string=string.lower()
    string= ''.join(filter(str.isalpha, string))
    
    left=0
    right=len(string)-1
    palindrome='YES'
    
    while left < right:
        if string[left] == string[right]:
            left=left+1
            right=right-1
        else:
            palindrome='NO'
            break
    return palindrome

print(is_palindrome("Madam, I'm Adam"))
print(is_palindrome('А роза упала на лапу Азора'))

"""# 6
Написать функцию ```calculate```, которая принимает на вход текстовый файл содержащий строки следующего формата:

Формат файла:
    ```арифметическая операция```    ```целое число #1```    ```целое число #2```\
Разделитель - 4 пробела

Функция должна вернуть 1 строку.
Строка содержит набор из чисел, разделенных запятой. 
После последнего числа запятая не ставится.
Каждое число - результат операции: 
    ```"результирующее целое число"``` = ```"целое число #1"``` применить ```"арифметическая операция"``` ```"целое число #2"```

**Пример входного файла:**

`+    5    4`\
`-    -10449    -7623`\
`**    2    10`

**Пример выходной строки (для примера входного файла выше):**

`9,-2826,1024`

**Допустимые операции:**

`+ (сложение)`\
`- (вычитание)`\
`* (умножение)`\
`// (целочисленное деление) (для этой операции подаются только положительные числа)`\
`% (остаток от деления) (для этой операции подаются только положительные числа)`'\
`** (возведение в степень) (для этой операции подаются только положительные числа)`

Входные числа - только целые.\
Выходные числа - только целые.

[Входной файл для самопроверки.](https://drive.google.com/file/d/1OcqaMTseYffO2JAF_thBJDJ-aqFq9Vxc/view?usp=sharing)

[Выходная строка для самопроверки содержится в файле.](https://drive.google.com/file/d/1IkCn8C6ULuEIngSSpkvI-0cIhDUiIEk9/view?usp=sharing)







"""

path2file='test_input_file_1.txt'
def calculate(path2file):
    with open (path2file, 'r', encoding='utf-8') as f:
        out=[]
        for line in f:
            lst=line.split()
            lst[1],lst[0] = lst[0],lst[1]
            lst=''.join(lst)
            res=eval(lst)
            out.append(res)
        out=', '.join(str(x) for x in out)
        return(out)

print(calculate(path2file))

"""# 7
Написать функцию ```substring_slice```,которой на вход поступают два текстовых файла.

- Первый файл содержит строки текста.   
 
- Второй файл содержит строки из двух целых неотрицательных чисел.
Первое число в строке всегда меньше или равно второму.
Числа всегда меньше длины соответствующей строки первого файла.
Соответствующей - это значит 1-ая строка из 1-го файла соответствует 1-ой строке из 2-го файла, а 123-я строка из 1-го файла соответствует 123-ей строке из 2-го файла.

- Функция должна вернуть строку, состоящую из подстрок 1-го входного файла.
Подстроки разделены пробелами.
Какие брать подстроки - написано во втором файле.
В конце файла пробела нет.

**Например**
120 строка в 1-ом файле: `JBOljrfkrfjgikenfjerkrkvkfKUGlknc`
120 строка во 2-ом файле: `13 27`
Это значит 120 подстрока в результирующем файле это символы с 13 по 27, включая 13-ый и 27-ой символы.
Не забывайте, что нумерация символов в строке с 0.
Пример требуемой подстроки: `kenfjerkrkvkfKU`
- **Пример 1-го входного файла:**
  ```
QxBpXEeyDWHiuTttWjhFMGTlrCMqpSvrNOQoxUbyiZombbLaYqBHvydPJlvdspwwpgeLNlHMVYrZvPsQkcQgPpierYSahialdXlde
rNsZEKdYYlKKRrYGNWEXTYXOpQqrdGANRfoyeVvRwLVhZDfzKhFQkuSYODIXFLYafnXbxuwqZKQKjSiFZAtSponvmulcjicIDhNaQ
TttSFLqbNkHvOeHSKTTGEEGxwtXImLeCmcKjvsIkIIvvlsUSazNuEsdDYlOljweSubVJxHbSJkBpByFiUCFctgrLKhlYgEWWuDYqx
```

- **Пример 2-го входного файла:**
```
30 84
5 79
70 70
```
- **Пример выходной строки:**
```
vrNOQoxUbyiZombbLaYqBHvydPJlvdspwwpgeLNlHMVYrZvPsQkcQgP KdYYlKKRrYGNWEXTYXOpQqrdGANRfoyeVvRwLVhZDfzKhFQkuSYODIXFLYafnXbxuwqZKQKjSiF b

```

[Пример 1-го входного файла для самопроверки.](https://drive.google.com/file/d/1XlnnBunKfNA2c4so3VKH1kXKvFjOLDAX/view?usp=sharing)

[Пример 2-го входного файла для самопроверки.](https://drive.google.com/file/d/1_gIyNhoSptvlvfA8UOlY60rXDva1fW2G/view?usp=sharing)

[Пример выходной строки для двух файлов выше содержится в этом файле.](https://drive.google.com/file/d/11Lsq1DV8iuMsZ_LPuTj50w5Htq1-95Ys/view?usp=sharing)
"""

path2file_1 = 'test_import_file_2_1.txt'
path2file_2 = 'test_import_file_2_2.txt'
def substring_slice(path2file_1,path2file_2):
     with open(path2file_1) as f1, open(path2file_2) as f2:
          with open("3.txt", "w")as f3:
               n1 = f1.read().splitlines()
               n2 = f2.read().splitlines()
               for i in range(len(n1)):
                   f3.writelines(n1[i] + ' ' + n2[i]+ '\n')
               
     with open('3.txt') as file:
          res=[]
          for line in file:
               line=line.split()
               start, end=int(line[1]), int(line[2])+1
               string=line[0]
               changed= string[start:end]
               res.append(changed)
          res=' '.join(str(x) for x in res)
          return(res)
print(substring_slice(path2file_1,path2file_2))

"""#8

Написать функцию ```decode_ch```,на вход которой поступает строка.В ней хранится набор химических символов (He, O, H, Mg, Fe, ...). Без пробелов.
Нужно расшифровать химические символы в название химических элементов.Функция должна вернуть строку - расшифровку

Для удобства, прилагается [json файл](https://drive.google.com/file/d/1Uugf4zLRjBx-73RfelroOrf1JlTtpLfi/view?usp=sharing), который ставит в соответствие химическому символу его химическое название.

Как прочитать этот файл в словарь python (dict):
```
periodic_table = json.load(open('periodic_table.json'))
```
- **Пример входной строки:**
```
NOTiFICaTiON
```
-**Пример выходной строки:**
```
АзотКислородТитанФторЙодКальцийТитанКислородАзот
```

Обратите внимание, что, например, "Bi" - это "Висмут", а не "БорЙод".
То есть регистр (заглавные или прописные) букв имеет значение.


"""

import json
periodic_table = json.load(open('periodic_table.json', encoding='utf-8'))

def decode_ch(sting_of_elements):
    encodedString = ''
    import re
    string= re.sub(r'([A-Z])', r' \1', sting_of_elements).split()
    for el in string:
        encodedString += periodic_table[el]
    return encodedString

sting_of_elements = input('Enter string: ')
encodedString = decode_ch(sting_of_elements)
print('Decoded string: ', encodedString)

"""#9

Создайте класс с названием Student.

При инициализации объекта подается два аргумента. Первый - имя студента. Второй - фамилия студента.

1. Создайте три атрибута объекта данного класса:

- *name* имя студента
- *surname* фамилия студента
- *fullname* имя и фамилия студента через пробел
2. Создайте метод для экземпляра класса Student под названием greeting, который при вызове возвращает строку Hello, I am Student
Здесь и далее нужно только написать сам класс. 
3. Добавьте новый атрибут класса под названием grades. При инициализации объекта соответственно добавляется новый аргумент, в котором будет лежать список оценок данного студента, по дефолту равный списку [3,4,5]. Создайте метод под названием mean_grade, который возвращает среднее всех оценок студента (то есть среднее этого атрибута).
4. Сделайте метод is_otlichnik, который возвращает строку YES, если средняя оценок студента больше или равна 4.5 и NO в противном случае.
Примечание: этот метод должен вызывать метод mean_grade внутри себя.
5. На этот раз определим операцию сложения для двух студентов. Пусть такая операция возвращает строку следующего вида: "Name1 is friends with Name2", где Name1 и Name2 - имена первого студента и второго (именно атрибут name). То есть, если создать два экземпляра класса Student, то их сумма должна вернуть вышеописанную строку.
6. Теперь переопределим поведение нашего класса с функцией print. Пусть при вызове функции print от экземпляра класса Student печатается его атрибут fullname.


"""

from statistics import mean
class Student:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.fullname= '{} {}'.format(name, surname)
        #print('Student exict') #for me
     
    def greeting(self): #метод экземпляра
        return 'Hello, I am '+ str(Student) 

    grades=[3,4,5] #не очень понимаю зачем нам атрибут класса, если мы его и так подаем каждому студенту подаем аргументом дефолт
    def __init__(self, name, surname, grades=[3,4,5]):
        self.name = name
        self.surname = surname
        self.fullname= '{} {}'.format(name, surname)
        self.grades =grades

    def mean_grade(self): 
        mg = mean(self.grades)
        return mg

    def is_otlichnik(self):   
        if self.mean_grade()>= 4.5:
            return 'YES'
        else:
            return 'NO'

    def __add__(self, other):
        if isinstance(other, Student):
            return '{Name1} is friends with {Name2}'.format(Name1=self.name, Name2=other.name)

    def __str__(self):
        return self.fullname




ob1= Student('Ben','Aren')
ob2= Student('Tom', 'Adams', [5,5,5])
print(ob2.is_otlichnik())
print(ob1.__add__(ob2))

"""#10

Определите  класс исключений ```MyError```,
 который принимает строковое сообщение ```msg``` в качестве параметра при инициализации и также имеет атрибут ```msg```.

Подсказка: Чтобы определить кастомный класс  исключения,нужно создавать класс, унаследованный от ```Exception```.


"""

class MyError(Exception):

     def __init__(self, msg):
          self.msg = msg

'''error example'''
def division_by_zero(x,y):
     if y==0:
         raise MyError('Division be zero!!!!')
     ans= 0
     while y!=0:
          ans= x/y
     return ans

