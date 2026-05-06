# .append - bu listni oxiriga faqat bitta qiymat qoshadi
mevalar = ["olma", "nok", "uzum"]
mevalar.append("gilos")
mevalar.append("shaftoli")
print(mevalar)

# .extend - bu listga bir nechta qiymatni qoshsa boladi
mevalar2 = ["olma", "nok", "uzum"]
mevalar2_1 = ["gilos", "shaftoli", "behi", "mandarin"]
mevalar2.extend(mevalar2_1)
print(mevalar2)

# .insert - bu listga indexni tanlab qiymat qoshish yani 2-indexning o'rniga qo'yadi, qolganlarini o'ngga suradi
mevalar3 = ["olma", "shaftoli", "nok"]
mevalar3.insert(2, "behi")
print(mevalar3)

# .pop - bu listdagi qiymatlarni ochiradi agar .pop ni ochiga hech narsa yozilmasa ong tomondan ochiradi
mevalar4 = ["olma", "nok", "behi"]
mevalar4.pop(1)
print(mevalar4)

# .remove - bu listagi qiymatni ochiradi va ikkta bir hil qiymat kelgan bolsa birinchi kelganini ochiradi
mevalar5 = ["olma", "behi", "nok"]
mevalar5.remove("behi")
print(mevalar5)

# .clear - bu listdagi hamma qiymatlarni ochirib tashlaydi
mevalar6 = ["olma", "beh", "nok"]
mevalar6.clear()

# .copy - bu listdagi qiymatlarni kochirib beradi
mevalar7 = ["nok", "olma", "banan"]
x = mevalar7.copy()
print(x)

# .count - bu listdagi nechta qiymat borligini aniqlaydi
mevalar8 = ["olma", "nok", "anor", "olma"]
x = mevalar8.count("olma")
print(x)

# .index - bu listdagi qiymatlarni index ni aniqlaydi
mevelar9 = ["olma", "banan", "nok", "anor"]
x = mevelar9.index("nok")
print(x)

# .sort - listdagi qiymatlarni kichikidan boshlab tartiblab beradi.  .sort(reverse=True) yozilsa kattasidan boshlab tartiblab beradi
sonlar = [3, 1, 5, 7, 9, 4]
sonlar.sort(reverse=True)
print(sonlar)

# .sort- agar sozlar kelsa.
ismlar = ["Oybek", "Jahongir", "Farruh", "Alisher"]
ismlar.sort(reverse=False)  # reverse=True bolsa alfavit boyicha teskari keladi False bolsa Alfavit boyicha keladi
print(ismlar)

# .reverse - listdagi qiymatlarni teskari o'girib beradi
ismlar = ["Nodir", "Aziz", "Oybek"]
ismlar.reverse()
print(ismlar)
