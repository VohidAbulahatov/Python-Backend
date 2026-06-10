# pythonda nusxa olishni ikki xil usuli bor:
# shallow copy
# deep copy

# deep copy
from copy import deepcopy

a = [1, 2, 3, 4, [5, 6]]
b = deepcopy(a)
b[4].append(7)
# print(a)

# Dictionary
# hash table -> dict
# CRUD -> Create, Read, Update, Delete

d = {"ism": "Vohid", "yoshi": 27}
d2 = dict(ism="Vohid", yoshi=27)
d3 = dict([("ism", "Vohid"), ("yoshi", 27)])
d["ball"] = 5  # yangi qiymat yaratish
# print(d)
# print(d2)
# print(d3)


# misol
harry_potter_dic = {
    "Harry Potter": "Gryffindor",
    "Ron Weasley": "Gryffindor",
    "Hermione Granger": "Gryffindor"
}
add_characters_1 = {
    "Albus Dumbledore": "Gryffindor",
    "Luna Lovegood": "Revenclaw"
}
harry_potter_dic.update(add_characters_1)  # update 2 dicni 1 chi dic ga qoshib yuboradi

add_characters_2 = [
    ["Draco Malfoy", "Slytherin"],
    ["Cedric Diggory", "Hufflepuff"]
]
harry_potter_dic.update(add_characters_2)

add_characters_3 = [
    ("Rubeus Hagrid", "Gryffindor"),
    ("Minerva McGonagall", "Gryffindor")
]
harry_potter_dic.update(add_characters_3)
del harry_potter_dic[
    "Minerva McGonagall"]  # del kalit va qiymatni ochiradi va faqat mavjud bolgan kalit yoki qiymatni ochiradi

# new = harry_potter_dic.get("Harry Potter",None)  # get koddan kalitni qidiradi
#
# print(new)
# print(harry_potter_dic)
# print(harry_potter_dic.items())
# print(harry_potter_dic.keys())
# print(harry_potter_dic.values())

from collections import Counter
counter= Counter(harry_potter_dic.values())
print(counter)
# Agar Minerva lug'atda bo'lsa o'chiradi, bo'lmasa xatolik bermay None qaytaradi
harry_potter_dic.pop("Minerva McGonagall", None)

