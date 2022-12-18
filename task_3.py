#1. Найти все числа от 1 до 1000, которые делятся на 17
list1=[i for i in range(1000) if i%17==0]
#print(list1)

#2. Найти все числа от 1 до 1000, которые содержат в себе цифру 2
list2=[i for i in range(1000) if "2" in str(i)]
#print(list2)

#3. Найти все числа от 1 до 10000, которые являются палиндромом
list3=[i for i in range(10000) if str(i)==str(i)[::-1]]
#print(list3)

#4. Посчитать количество пробелов в строке 
string4=" random  string with    some s p a c  e s ! " 
ans4=list(string4).count(" ")

#5. Есть любая последовательность непробельных символов латинского алфавита, удалить все гласные из этого слова
string5="abdegjrutopqmcnfiyiyyikpqwzp"
vowels="aeiouy"
ans5="".join(i for i in string5 if i not in vowels)

#6. На входе строка со словами, разделенными через 1 пробел. Найти все слова, длина которых не больше 5
string6 = "A simple sentence has the most basic elements that make it a sentence: a subject a verb and a completed thought"
ans6="\n".join(i for i in string6.split() if len(i)<6)
#print(ans6)

#7. На входе строка со словами, разделенными через 1 пробел. Получить словарь, 
# где в качестве ключа используется само слово, а в значении длина этого слова.
string7 = "A simple sentence has the most basic elements that make it a sentence: a subject a verb and a completed thought"
ans7={x: len(x) for x in string7.split()}
#print(ans7)

#8. На входе предложение со всеми пробельными и непробельными символами латинского алфавита. 
# Получить словарь используемых букв в строке, то есть на выходе список уникальных букв.
string8=" ##)_:_OI(#@#$@PSAMK,jasbdaubgha k Ka  ama 0~-=!20fZz12ak"
ans8 = {c.upper() for c in string8 if c.isalpha()}
#print(ans8)

#9. На входе список чисел, получить список квадратов этих чисел 
list9=[2,6,3,2,13,-1,0,2, 1.2, 0.7]
ans9=[i**2 for i in list9]
ans9_2=list(map(lambda x: x**2, list9))

#10. На входе список координат, например, [(1, 1), (2, 3), (5, 3)]. Найти все точки, которые принадлежат прямой y = 5 * x - 2. 
#На выходе получить словарь из самой точки и расстоянии до этой точки из начала координат (0, 0)
coords=[(1, 1), (2, 3), (2, 8),(5, 3), (1, 3)]
line=[(x,y) for x, y in coords if y==5*x-2]
dist=[(x**2+y**2)**0.5 for x,y in line]
ans10=dict(zip(line, dist))

#11. Возвести в квадрат все четные числа от 2 до 27. На выходе список.
ans11=[i for i in range(2, 27) if i%2==0]
#print(ans11)

#12. На входе список из координат точек на плоскости. Найти расстояние до самой удаленной точку от начала координат (0, 0) в первой четверти 
coords=[(1, 1), (2, 3), (5,-2),(-1,-1),(2, 8),(5, 3),(-5,3), (1, 3)]
dist=[(x**2+y**2)**0.5 for x,y in coords if x>0 and y>0]
#print(max(dist))

#13. На входе два списка чисел nums_first = [1, 2, 3, 5, 8] и nums_second = [2, 4, 8, 16, 32]. 
# Получить пары сумм и разниц, [(3, -1), (6, -2), (11, -5), ...]
nums_first = [1, 2, 3, 5, 8]
nums_second = [2, 4, 8, 16, 32]
ans13=[(i+j, i-j) for i, j in zip(nums_first, nums_second)]
#print(ans13)

#14. На входе список строк из чисел, например, ['43141', '32441', '431', '4154', '43121']. Найти четные квадраты этих чисел. 
# Ответ записать снова в список из строк, то есть сформировать обратно список строк, но уже отфильтровать все четные квадраты.
str14=['43141', '32442', '431', '4154', '43121']
ans15=[i for i in str14 if ((int(i)**2)%10)%2==0]
#print(ans14)


#15. Менеджер как обычно придумал свое представление данных, а нам оно не подходит

input_str = """name,Petya,Vasya,Masha,Vova
grade,5,5,8,3
subject,math,language,physics,math
year,1999,2000,1995,1998"""

lst=[i.split(",") for i in input_str.split()]
ans15=[i for i in zip(*lst)]
print(ans15)

#16. Получить сумму по столбцам у двумерного списка

a = [[11.9, 12.2, 12.9],
    [15.3, 15.1, 15.1], 
    [16.3, 16.5, 16.5],
    [17.7, 17.5, 18.1]]
ans16=[sum(i) for i in zip(*a)]    
print(ans16) 