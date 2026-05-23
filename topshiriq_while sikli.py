# 1 topshiriq
qator = 1
while qator <= 5:
    ustun = 1
    while ustun <= qator:
        print(qator, end="")
        ustun += 1
    print(qator)
    qator += 1

# 2 topshiriq
user_1 = int(input("son kiriting: "))
yigindi = 0
while user_1 > 0:
    raqam = user_1 % 10
    yigindi += raqam
    user_1 = user_1 // 10
print(f"raqamlar yigindisi:{yigindi}")

# 3 topshiriq
son = 1
yigindi_1 = 0
while son <= 100:
    if son % 2 != 0:
        yigindi_1 += son
    son += 1
print(f"1 dan 100 gacha toq sonlar:{yigindi_1}")

# 4 topshiriq
user_2 = [2, 43, 5, 77, 88, 323, 46, 86, 7, 19]
kichik = 0
katta = 0
i = 0
while i < len(user_2):
    son_1 = user_2[i]
    if son_1 > katta:
        kichik = katta
        katta = son_1
    elif son_1 > kichik:
        kichik = son_1
    i += 1
print(f"eng katta son:{katta}")

# 5 misol
import random

tasodifiy_son = random.randint(1, 100)
while True:
    tahmin = int(input("tahminiy raqam kiriting: "))
    if tahmin == tasodifiy_son:
        print("tariklaymiz topdingiz")
        break
    elif tahmin>tasodifiy_son:
        print("juda baland")
    else:
        print("juda past")

