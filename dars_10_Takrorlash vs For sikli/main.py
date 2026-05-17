"""Foydalanuvchidan qiziqishlari so'ralsin.
Agar kitob yoki kutubxona qiziqishlari orasida bolsa, qanday kitoblar yoqishini so'ralsin.
   agar detektiv sozini ishlatsa, "shaytanat" kitobi haqida fikr soralsin.
   agar diniy kitoblarga qiziqsa "hadis va hayot" kitoblar toplami sovg'a qilamiz deyilsin.
Agar sport sozi qiziqishlari orasida bolsa, qaysi sport turiga qiziqishi soralsin,
   agar futbol sport turlari orasida bolsa, qaysi komandani yoqtirishini soralsin.
   agar real yoki barcelona komandasi yozsa, el-classicoga chipta sovg'a qilamiz deyilsin.
"""
from pyexpat import native_encoding

# qiziqish = input("Iltimos, qiziqishlaringizni kiriting (kitob yoki sport): ").lower()

# 1. Kitob bo'limi
# if "kitob" in qiziqish or "kutubxona" in qiziqish:
#     qiziqish_1 = input("Qanday kitoblar yoqadi? ").lower()
#
#     if "detektiv" in qiziqish_1:
#         # Bu yerda input shunchaki savol berish uchun, javobni tekshirmasa ham bo'ladi
#         input("'Shaytanat' kitobi haqida fikringiz qanday? ")
#         print("Tushunarli, qiziqarli fikr!")
#     elif "diniy" in qiziqish_1:
#         print("Sizga 'Hadis va Hayot' kitoblar to'plamini sovg'a qilamiz!")
#     else:
#         print("Bu janr ham juda ajoyib ekan!")
#
# # 2. Sport bo'limi
# elif "sport" in qiziqish:
#     sport_1 = input("Qaysi sport turiga qiziqasiz? ").lower()
#
#     if "futbol" in sport_1:
#         futbol = input("Qaysi komandani yoqtirasiz? ").lower()
#         if "real" in futbol or "barca" in futbol or "barcelona" in futbol:
#             print("Sizga El-Classico uchun chipta sovg'a qilamiz!")
#         else:
#             print("Undan ko'ra futbol ko'rmaganingiz ma'qul (hazil).")
#     else:
#         print(f"{sport_1.capitalize()} bilan shug'ullanish juda foydali!")
#
# # 3. Agar foydalanuvchi umuman boshqa narsa yozsa
# else:
#     print("Kechirasiz, men hozircha faqat kitoblar va sport haqida suhbatlasha olaman.")

# sikl - loop
"""
1- sikl turi: For sikli
Break - siklni toxtatadi
Continue - siklni keyingi elementga otkazib yuboradi
2- sikl turi: While 
"""
# mevlar = ["olma", "uzum", "gilos", "nok"]
# for item in mevlar:
#     if item == "gilos":
#         continue
#     print(item, "sharbati")

# misol
# m=["a","b","c","d","e"]
# for i in range(0,5,2):
#     print(f"{m[i]} ning indeksi {i}")

# misol
# m = ["a", "b", "a", "c", "e", "d", "a", "e"]
# natija = []
# for i in m:
#     if i not in natija:
#         natija.append(i)
# print(natija)

# misol
# kg = 5000
# # for vazn in range(1, 10):
# #     print(f"{vazn} kg narhi {kg * vazn}")

# misol
# son = int(input("son: "))
# natija = 1
# for i in range(1, son + 1):
#     natija = natija * i
# print(natija)

# misol
import math

son = int(input("son: "))
chegara = int(math.sqrt(son))
for i in range(2, chegara + 1):
    if son % i == 0:
        print("tub son emas")
        break
else:
    print("tub son")
