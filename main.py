# string metodlar
# malum obyekt, kalssga tegishli funksiya metod deyiladi

# s = "salom dunyo"
# s2 = s.capitalize() #stringni bosh harfini kattalashtirish
# print(s2)

# s = "Salom Dunyo"
# s2 = s.casefold()  # stringni har bitta sozini bosh harfini kiciklashtirish
# print(s2)

# s = "Salom Dunyo"
# s2 = s.center(40, "*")  # stringni ortaga yani markazga olib keladi va qavus ochib qandaydir sozlar qoshsa boladi
# print(s2)

# s = "salom dunyo hammaga salom"
# s2 = s.count("salom")  #count ichiga yozilgan sozlar yoki raqamlarni nechtaligini sanaydi
# print(s2)

# s = "salom dunyo hammaga salom."
# s2 = s.endswith(".") #stringni nima bilan tugaganini true or false beradi
# print(s2)

# s = "salom dunyo hammaga salom."
# s2 = s.find("hammaga") #stringni index ga qarab qayerda turganini topadi
# s.index("") index ham shu ishni qiladi
# print(s2)

# s = "Salom22"
# s2 = s.isalnum() #harf va raqamlarni topsa true qaytaradi kelmasa false qaytaradi
# print(s2)

# s = "Salom22"
# s2 = s.isascii() #shu sozlar ascii jadvalida bor bolsa true yoq bolsa false chiqaradi
# print(s2)

# myTuple = ("Salom", "Hayr", "Nechi")
# s2 = "-".join(myTuple)  #myTuple qoshish yani birlashtirish stringa otkazib ham beradi
# print(s2)

# s = "Salom qandasizlar zormi"
# s2 = s.split() #stringni listga o'girib beradi
# print(s2)

s = "    Salom qandasizlar zormi    "
s2 = s.strip() #stringdagi boshi va oxiridagi bosh joylarni olib tashlaydi
print(s2)

s = "    Salom qandasizlar zormi    "
s2 = s.replace("zormi","yaxshimi") #stringdagi sozlarni almashtirish
print(s2)