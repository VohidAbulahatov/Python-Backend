# While sikli
from operator import index
# from tabnanny import Whitespace

# sanoq = 0
# while sanoq < 5:
#     print("Hello world")
#     sanoq += 1  # sanoq = sanoq + 1

# misol
# while True:
#     ism= input("ism: ")
#     print(f"Hello {ism}")
#     if ism == "john":
#         print("Ozbekcha ism emas")
#         break


# misol
# users = ["Aziz", "Ali", "Vohid", "Farruh"]
# password = "qwerty"
# while True:
#     ism = input("ism: ")
#     parol = input("parol: ")
#     if ism in users and parol == password:
#         print("Ruhsat etildi Xush kelibsiz")
#         break
#     else:
#         print("Xato qayta urinib koring")

# oyin yaratish
# g = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# belgi = "X"
#
# while True:
#     print(f"""
#     {g[0]} | {g[1]} | {g[2]}
#     ----------
#     {g[3]} | {g[4]} | {g[5]}
#     ----------
#     {g[6]} | {g[7]} | {g[8]}
#     """)
#
#     user1 = int(input(f"{belgi} o'yinchi, raqam kiriting: "))
#
#     # Yangi xatosiz shartimiz:
#     if 1 <= user1 <= 9 and g[user1 - 1] != "X" and g[user1 - 1] != "0":
#         g[user1 - 1] = belgi
#
#         # 1. G'OLIBNI TEKSHIRISH (Barcha 8 ta holat)
#         if (g[0] == g[1] == g[2] or  # gorizontal
#                 g[3] == g[4] == g[5] or
#                 g[6] == g[7] == g[8] or
#                 g[0] == g[3] == g[6] or  # vertikal
#                 g[1] == g[4] == g[7] or
#                 g[2] == g[5] == g[8] or
#                 g[0] == g[4] == g[8] or  # diagonal
#                 g[2] == g[4] == g[6]):
#             # Oxirgi o'zgargan doskani ko'rsatish uchun print qilamiz
#             print(
#                 f"\n{g[0]} | {g[1]} | {g[2]}\n----------\n{g[3]} | {g[4]} | {g[5]}\n----------\n{g[6]} | {g[7]} | {g[8]}")
#             print(f"\nTabriklaymiz! {belgi} o'yinchi g'olib bo'ldi!")
#             break  # O'yin tugadi, tsiklni to'xtatamiz
#
#         # 2. NAVBATNI ALMASHTIRISH
#         if belgi == "X":
#             belgi = "0"
#         else:
#             belgi = "X"
#     else:
#         print("Noto'g'ri yoki band katakni tanladingiz! Qaytadan urinib ko'ring.")


# Hangman oyini
import random

word_list = ["apple", "data", "case", "banana", "peach", "key"]
word = random.choice(word_list)
tahminlar = set()
xatolar = 0
max_xatolar = 6  # O'yinchi necha marta xato qilishi mumkin

print("Hangman o'yiniga xush kelibsiz!")

while xatolar < max_xatolar:
    display = ""
    for letter in word:
        if letter in tahminlar:
            display += letter
        else:
            display += "_"

    print(f"\nSo'z: {display}")
    print(f"Qolgan imkoniyat: {max_xatolar - xatolar}")

    if "_" not in display:
        print("Tabriklaymiz, siz yutdingiz!")
        break

    tahmin = input("Harf kiriting: ").lower()

    if tahmin in tahminlar:
        print("Bu harfni avval kiritgansiz.")
        continue

    tahminlar.add(tahmin)

    if tahmin not in word:
        xatolar += 1
        print(f"Afsus, '{tahmin}' so'zda mavjud emas.")
    else:
        print(f"Barakalla! '{tahmin}' so'zda mavjud.")

else:
    print(f"\nO'yin tugadi! Siz yutqazdingiz. To'g'ri so'z: {word}")
