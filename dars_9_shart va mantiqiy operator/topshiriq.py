# # 1 vazifa
# obhavo = int(input("ob-havo haroratini yozing: "))
# if obhavo < 0:
#     print("Sovuq")
# elif obhavo >= 0 and obhavo <= 20:
#     print("Salqin")
# elif obhavo >= 21 and obhavo <= 30:
#     print("Iliq")
# elif obhavo >= 31:
#     print("Issiq")

# 2 vazifa
# summa = int(input("Xarid summangizni yozing: "))
#
# if summa < 50000:
#     print("Chegirma yo'q")
#     yakuniy_narx = summa
# elif summa <= 100000:  # 50,000 dan 100,000 gacha
#     chegirma = summa * 0.05
#     yakuniy_narx = summa - chegirma
#     print(f"5% chegirma: {chegirma} so'm")
# else:  # 100,000 dan yuqori hamma holatlar
#     chegirma = summa * 0.10
#     yakuniy_narx = summa - chegirma
#     print(f"10% chegirma: {chegirma} so'm")
#
# print(f"To'lanadigan yakuniy summa: {yakuniy_narx} so'm")

# 3 vazifa
# login=input("Loginingizni kiriting: ")
# parol= input("Parolingizni kiriting ")
# if login== "admin" and parol== "12345":
#     print("Xush kelibsiz,admin!")
# else:
#     print("Login yoki parol xato")

# 4 vazifa
# yosh=int(input("Yoshingizni kiriting: "))
# if yosh<13:
#     print("Sizga ushbu film tavsiya etilmaydi")
# elif yosh<=17:
#     print("Siz filmni ota-onangiz bilan korishingiz mumkin")
# elif yosh>=18:
#     print("Siz filmni tomosha qilishingiz mumkin")

# 5 vazifa
# print("--RESTORAN MENYUSI--")
# print("1- osh")
# print("2- mastava")
# print("3 - shashlik")
# tanlov = input("Taom raqamini tanlang: ")
# if tanlov == "1":
#     print("Taom:Osh")
#     print("Narhi:30,000 so'm")
#     print("Tayyorlanish vaqti: Tayyor(bor)")
# elif tanlov == "2":
#     print("Taom:Mastava")
#     print("Narhi:25,000 so'm")
#     print("Tayyorlanish vaqti: 10 daqiqa")
# elif tanlov == "3":
#     print("Taom:Shashlik")
#     print("Narhi:16,000 so'm(1 donasi)")
#     print("Tayyorlanish vaqti: 20 daqiqa")
#
# else:
#     print("Xato! Menyuda bunday taom yoq")

# 6 vazifa
# email = input("Email manzilingizni kiriting: ")
#
# # Ikkala belgi ham borligini tekshiramiz
# if email.find('@') != -1 and email.find('.') != -1:
#     print("Email qabul qilindi")
# else:
#     print("Noto'g'ri email manzil kiritildi")

# if "@" in email and "." in email:
#     print("Email qabul qilindi")

# 7 vazifa
# print("---Ballar tizmi---")
# print("86 dan 100 gacha: 5 baho")
# print("70 dan 85 gacha: 4 baho")
# print("55 dan 69 gacha: 3 baho")
# print("55 dan past: 2 baho")
# ball = int(input("Siz olgan ballingizni kiriting(0-100): "))
# if ball > 100 or ball < 0:
#     print("Xato! Ball 0 va 100 oralig'ida bolishi kerak")
# elif ball >= 86 and ball <= 100:
#     print("Bahongiz 5")
# elif ball >= 70:
#     print("Bahongiz 4")
# elif ball >= 55:
#     print("Bahongiz 3")
# elif ball < 55 and ball >= 0:
#     print("Bahongiz 2")
# else:
#     print("Xato! manfiy ball kiritish mumkin emas")

# 8 vazifa
# summa = int(input("Kartangizdagi summani kiriting: "))
# summa2 = int(input("Yechib olmoqchi bolgan summanignizni kiriting: "))
# if summa < summa2:
#     print("Hisobda yetarli mablag' mavjud emas")
# elif summa2 < 5000:
#     print("Minimal yechish summasi 5000 so'm")
# else:
#     qoldiq = summa - summa2
#     print("Pul muvaffaqiyatli yechildi")
#     print(f"Siz {summa} so'm yechdingiz. Hisobingizda {qoldiq} so'm qoldi.")

# 9 vazifa
# kun = input("Bugun qaysi kunligini kiriting: ")
# if kun.capitalize() == "Shanba" or kun.capitalize() == "Yakshanba":
#     print("Bugun dam olish kuni")
# else:
#     print("Bugun ish kuni")

# 10 vazifa
tarif = int(input("Siz oyiga qancha internet trafigi ishlatasiz(GB da):"))
if tarif < 1:
    print("Sizga 'Mini' tarif mos keladi")
elif tarif < 5:
    print("Sizga 'Standart' tarifi mos keladi")
elif tarif >= 5:
    print("Sizga 'Unlimited' tarifi mos keladi")
