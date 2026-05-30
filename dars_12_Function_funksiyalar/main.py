# funksiyalar
from pyexpat import native_encoding


# def prints_5_hello():
#     for i in range(5):
#         print("Hello world")
# prints_5_hello()
# print("-----------")
# prints_5_hello()

# misol
# def sanoq():
#     for i in range(1, 40):
#         if i % 2 == 0 and i % 3 == 0:
#             print(i, end='  ')


# (sanoq())


# misol
# def add(a, b): # a va b bu yerda parametrlar
#     return a + b
#
#
# yigindi = add(5, 4) # 5 va 4 esa argentlar
# print(yigindi)


# misol
# login = "admin1"
# parol = 12345
# def login_print(l,p):
#     print(f"""
#     *************************
#     *                       *
#     * login: {l}         *
#     * parol: {p}          *
#     *                       *
#     *************************
# """)
# login_print(login,parol)


# misol
# def find_letter_count(word,letter):
#     return word.count(letter)
# natija= find_letter_count("wordinwordanotherword","word")
# print(natija)


# misol
# Oylar va sotuv hajmlari ko'rsatilgan lug'at (dictionary)
umumiy_narhlar = {
    "yanvar": 2000,
    "mart": 6000,
    "aprel": 15000,
    "sentabr": 9000,
    "dekabr": 10000
}
# 1. Funksiyani e'lon qilamiz va u "sales" degan lug'atni qabul qiladi
def big_sales(sales):
    # 2. Eng katta sotuv summasini saqlash uchun o'zgaruvchi (boshida 0 deb olamiz)
    max_sale = 0
    # Eng ko'p sotuv bo'lgan oy nomini saqlash uchun bo'sh matn (string) ochamiz
    max_month = ""

    # 3. Lug'at ichidagi har bir elementni (kalit va qiymatni) aylanib chiqamiz
    # month - oy nomi (key), amount - sotuv summasi (value)
    for month, amount in sales.items():

        # 4. Agar joriy oyning sotuvi biz bilgan eng katta sotuvdan ham katta bo'lsa:
        if amount > max_sale:
            # Yangi eng katta sotuv summasini eslab qolamiz
            max_sale = amount
            # Shu summaning oy nomini ham yangilab qo'yamiz
            max_month = month

    # 5. Sikl to'liq tugagach, eng katta sotuv bo'lgan oy nomini qaytaramiz
    return max_month


# Funksiyani umumiy_narhlar lug'ati bilan chaqiramiz va natijani o'zgaruvchiga olamiz
natija = big_sales(umumiy_narhlar)

# Natijani konsolga chiqaramiz
print("Eng ko'p sotuv bo'lgan oy:", natija)




# tepadagi misolni 2 chi varianti sodda
# Oylar va sotuvlar ko'rsatilgan lug'at
umumiy_narhlar = {
    "yanvar": 12000,
    "mart": 6000,
    "aprel": 15000,
    "sentabr": 9000,
    "dekabr": 10000
}

# max() funksiyasi va key=d.get yordamida eng qisqa yechim
def find_max_2(d):
    return max(d, key=d.get)

# Funksiyani chaqiramiz va natijani konsolga chiqaramiz
print(find_max_2(umumiy_narhlar))





















