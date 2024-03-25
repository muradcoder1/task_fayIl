# task1
# import time
# today=time.strftime("%d:%m:%Y %H:%M:%S")
# print(today)
# task2
#  from math import pi
# r=int(input("r - i giriniz:"))
# print((r**2)*pi)
# task3
# name=input("adı giriniz:")
# last_name=input("soyadı giriniz")
# print(f"{name}" "   " f"{last_name}")
# task4
# listi=int(input("listi giriniz :"))
# list = listi.split(",")
# tuple = tuple(list)
# print('List : ', list)
# task5
# color_list = ["Qırmızı","Yaşıl","Ağ" ,"Qara"]
# print(color_list[0],color_list[-1])
# task6
# n=int(input("1 deger giriniz"))
# nn=int(input("2 deger giriniz"))
# nnn=int(input("3 deger giriniz"))
# print(n+nn+nnn)
# task7
# from math import pi 
# r=int(input("r - i giriniz :"))
# V=4/3*pi*r**3
# print(V)
# task8
# import calendar
# year=int(input("1 yil girin"))
# month=int(input("1 ay giriniz"))
# print(calendar.month(year,month))
# task9
# import calendar
# year=int(input("1 yil girin"))
# month=int(input("1 ay giriniz"))
# d=print(calendar.Day(year,month))
# a=int(input("2 ci yiligiriniz"))
# b=int(input("2 ci ayi giriniz"))
# c=print(calendar.Day(a,b))
# print(d-c)
# task10
# import math
# x1=int(input(" x1 - i giriniz"))
# x2=int(input("x2 - i giriniz"))
# y1=int(input("y1 - i giriniz"))
# y2=int(input("y2 - i giriniz"))
# ikinöqtə_arasımdakı_mesafe=math.sqrt((x2-x1)**2+(y2-y1)**2)
# print(ikinöqtə_arasımdakı_mesafe)
# task11
# x = 4
# y = 3
# print((x + y) * (x + y))
# task12
# def fun():
#     name,age="Murad",22
#     adress="Azərbaycan Tovuz rayonu *"
#     print(name,age,adress)
# fun()
# task13
# a=int(input("1 - ci tam ededi giriniz :"))
# b=int(input("2 - ci tam ededi giriniz   :"))
# if a==int and b==int :
#       print("işlem başarılı")    yeniden baxxxx
# task14
# def tam_eded(x,y):
#     if x==y or x-y==5 or x+y==5:
#         return True
#     else:
#         return False
# print(tam_eded(3,3))
# task15
# def cem(x,y):
#     sum=x+y
#     if   sum>=15 and sum<=20:
#         return 20
#     else:
#         return False
# print(cem(11,7))
# task16
# def cem(x,y,z):
#     sum=x+y+z
#     if x==y or x==z or y==z:
#         return 0
#     else:
#         return sum
# print(cem(2,6,2))
# task17
# en boyuk ortaq bolen
# tsak18
# en kicik ortaq bolen
# tsak19
# b=int(input("uc bucagin terefini giriniz"))
# h=int(input("uc bucagin hundurluyunu giriniz"))
# S=1/2*h*b
# print(S)
# tsak20
# color_list_1 = set(["Ağ", "Qara", "Qırmızı"])
# color_list_2 = set(["Qırmızı", "Yaşıl"])
# print(color_list_1.difference(color_list_2))
# tsak21
# ədədlər = [    
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
#     958,743, 527
#     ]
# for i in ədədlər:
#       if i==237:
#             break
#       elif i%2==0:
       
#        print(i)
# tsak22
# def concatenate_list_data(a):
#     result = ''    
#     for element in a:
#         result += str(element) 
#     return result 
# print(concatenate_list_data([1, 5, 12, 2]))
# tsak23
# def fun(a):
#     n=int(input("bir sayi giriniz"))
#     for i in a:
#         if n==i:
#             return True
#     return False
# print(a([1, 5, 8, 3], n))
# tsak24
# n=int(input("isdediyiniz rakami giriniz   :"))
# if n==0:
#     print("0 - ir ne tek ne cutdur")
# elif n%2==0:
#     print("girdiyiniz rakam cutdur    :")
# else:
#     print("girdiyiz rakam tekdir  :")
# tsak25
# def uc_eded(a,b,c):
#      sum=a+b+c
#      if a==b==c:
#         sum=sum*3
#      return sum
# print(uc_eded(4,8,9)) 
# print(uc_eded(8,8,8))
# sartler forlar whleler aid tasklar
# tsak26 Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).
# for i in range(1500,2701):
#     if i%5==0 and i%7==0:
#         print(i)
#    task27     Write a Python program to convert temperatures to and from Celsius and Fahrenheit.
# [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
# Expected Output :
# 60°C is 140 in Fahrenheit
# 45°F is 7 in Celsius
# a=int(input("c ye cevirmek isdediyiniz rakami giriniz"))
# b=int(input("f ye cevirmek isdediyiniz rakami giriniz"))
# C=(5(a-32))/9
# F=(9*b+(32*5))/5
# print(C)
# print(F)
# task28
# import random
# a, m = random.randint(1, 10), 0
# while a != m:
#     b = int(input('tahmin etmek isdedi8i9zniz rakami girniz : '))
# print('Well guessed!') 
n=input("tersine cevirmek isdediyiniz sozu giriniz")
n.
print(n)