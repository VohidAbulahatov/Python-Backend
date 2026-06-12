# Set -> toplam

thisset = {"apple", "banan", "cherry", "apple"}  # setni dublikat qilib bolmaydi
# print(thisset)


thisset2 = {"apple", "banan", "cherry", "apple"}
# print(len(thisset2))


set_1 = {"iphone", "samsung", "nokia"}
set_2 = {"lg", "motorolla", "byd"}
set_1.update(set_2)  # 2 ta setni bir biriga qoshish
# print(set_1)


set_3 = {"iphone", "samsung", "nokia"}
set_4 = {1, 2, 3, 4, 5}
set_5 = set_3.union(set_4)
# print(set_5)


set_6 = {"apple", "cherry", "banan"}
set_7 = {"peach", "apple", "watermelon"}
set_6.intersection_update(set_7)  # ikkalasida ham  bir hil qiymat bolsa qaytaradi
print(set_6)



