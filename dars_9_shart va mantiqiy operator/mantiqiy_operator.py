# String and List Slicing - String va Listlarni kesish
# matn = "Hammaga salom"
# matn2 = matn[0:7]
# print(matn2)
from platform import python_branch

# Shart operatorlari - Conditions : if elif else
# print("Saylovga xush kelibsiz!")
# user = input("Ismingiz: ")
# age = int(input("Yoshingiz: "))
# print(f'Foydalanuvchi:{user},yoshi:{age}')
# if age < 18:
#     print("Yoshingiz yetmaydi, ruhsat yoq")
# else:
#     print("Xush kelibsiz!")

# print(15 == 15)  # True teng
# print(15 != 15)  # False teng emas
# print(15 <= 10)  # False kichik yoki teng
#
# arr = [1, 3, 4, 5, 7, 15]
# print(7 in arr)  # 7 arr ni ichida bormi True
# print(7 not in arr)  # 7 arr ning ichida emasmi False
#
# arr2 = [1, 4, 6, 8, 2, 33, 11, 66, 54]
# if 11 in arr2:
#     print("mavud")
# else:
#     print("mavjud emas")

# 1 chi variant
# yosh = int(input("yoshingizni kiriting:"))
# if yosh < 18:
#     print("voyaga yetmagan")
# elif yosh >= 18 and yosh < 30:
#     print("yosh avlod")
# elif yosh >= 30 and yosh < 45:
#     print("o'rta yosh")
# elif yosh >= 45 and yosh < 80:
#     print("qariya")
# else:
#     print("siz uzoq umr koruvchisiz :)")

# 2 chi sodda variant
# if yosh < 18:
#     print("voyaga yetmagan")
# elif yosh < 30:  # 18 dan kattaligi aniq, faqat 30 dan kichikligini tekshiramiz
#     print("yosh avlod")
# elif yosh < 45:
#     print("o'rta yosh")
# elif yosh < 80:
#     print("qariya")
# else:
#     print("siz uzoq umr ko'ruvchisiz :)")

# login = "admin"
# parol = "qwerty"
# user_login = input("login kiriting: ")
# user_parol = input("parol kiriting: ")
# if user_login == login and user_parol == parol:
#     print("ruhsat")
# else:
#     print("login yoki parol xato")

# 5 misol
# a=int(input("A:"))
# b=int(input("B:"))
# if a>3 and b<=6:
#     print(True)
# else:
#     print(False)

# 9 misol
# a = int(input("A: "))
# b = int(input("B: "))
# c = int(input("C: "))
# if a < b < c:
#     print("Rost")
# else:
#     print("Yolg'on")

# 15 misol
# a = int(input("A:"))
# if a % 2 == 0:
#     print("Juft son")
# else:
#     print("Toq son")

# 17 misol
# a = int(input("A:"))
# if a % 2 == 0 and len(str(a)) == 2:
#     print("Rost")
# else:
#     print("yolgon")

# 19 misol
# Foydalanuvchidan sonni qabul qilamiz
# son = int(input("Uch xonali son kiriting: ")) # Masalan: 454
#
# # Matematik ajratish
# a = son // 100        # 4
# b = (son // 10) % 10  # 5
# c = son % 10          # 4
#
# # Tekshirish
# if a != b and a != c and b != c:
#     print("Natija: True (Hamma raqamlar har xil)")
# else:
#     print("Natija: False (Kamida ikkita raqam bir xil)")

son = int(input("son: "))
if son == 1:
    print("Dushanba")
elif son == 2:
    print("Seshanba")
elif son == 3:
    print("Chorshanba")
elif son == 4:
    print("Payshanba")
elif son == 5:
    print("Juma")
elif son == 6:
    print("Shanba")
elif son == 7:
    print("Yakshanba")
else:
    print("Bundan hafta kuni yoq")
