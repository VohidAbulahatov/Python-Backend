txt1 = "salom"
print(txt1.capitalize())  # Salom

txt2 = "Salom Dunyo"
print(txt2.casefold())  # salom dunyo

txt3_1 = "Hammaga salom"
txt3_2 = "Hammaga salom"
txt3_3 = "Hammaga salom"

print(txt3_1.center(20))  # Hammaga salom
print(txt3_2.center(40, "*"))  # *************Hammaga salom**************
print(txt3_3.center(60))  # Hammaga salom

txt4 = "My name is Vohid"
print(txt4.count("Vohid"))  # 1

txt5 = "read and write."
txt5_2 = "read and write"
print(txt5.endswith("."))  # True
print(txt5_2.endswith("."))  # False

txt6 = "My name is Vohid"
txt6_1 = "My name is Vohid"
print(txt6.find("is"))  # 8
print(txt6_1.find("Abror"))  # -1

txt7 = "noname77gmail"
txt7_1 = "noname77@gmail.com"
print(txt7.isalnum())  # True
print(txt7_1.isalnum())  # False

txt8 = "Salom44"
txt8_1 = "|?||"
print(txt8.isascii())  # True
print(txt8_1.isascii())  # True

txt9 = ("ruchka", "qalam", "daftar")
print("---".join(txt9))  # ruchka---qalam---daftar

txt10 = "Hayrli kech hammaga"
print(txt10.split())  # ['Hayrli', 'kech', 'hammaga']

txt11 = "     Hammaga salom     "
print(txt11.strip())  # Hammaga salom

txt12 = "My name is Vohid"
print(txt12.replace("Vohid", "Abror"))  # My name is Abror

txt13 = "H\ta\tm\tm\ta\tg\ta"
print(txt13.expandtabs())  # H       a       m       m       a       g       a
print(txt13.expandtabs(5))  # H    a    m    m    a    g    a
print(txt13.expandtabs(10))  # H         a         m         m         a         g         a

txt14 = "My name is {fname}, I'm {age}"
txt14_1 = "My name is {0}, I'm {1}"
txt14_2 = "My name is {}, I'm {}"
txt14_3 = "For only {price:.2f} dollars!"
print(txt14.format(fname="Vohid", age=26))  # My name is Vohid, I'm 26
print(txt14_1.format("Vohid", 26))  # My name is Vohid, I'm 26
print(txt14_2.format("Vohid", 26))  # My name is Vohid, I'm 26
print(txt14_3.format(price=59))  # For only 59.00 dollars!

txt15 = "Hammaga salom"
print(txt15.index("s"))  # 8

txt16 = "hammagasalom"
txt16_1 = "hammaga salom"
print(txt16.isalpha())  # True
print(txt16_1.isalpha())  # False

txt17 = "1234910"
txt17_1 = "1234-1234"
print(txt17.isdecimal())  # True
print(txt17_1.isdecimal())  # False

txt17 = "1234910"
txt17_1 = "1234DFH1234"
print(txt17.isdigit())  # True
print(txt17_1.isdigit())  # False

txt18 = "88"
print(txt18.zfill(5))  # 00088

txt19 = "Hayrli kech hammaga"
print(txt19.upper())  # HAYRLI KECH HAMMAGA

mydict = {83: 80}
txt20 = "Hi Sam"
print(txt20.translate(mydict))  # Hi Pam

txt21 = "my name is vohid"
print(txt21.title())  # My Name Is Vohid

txt22 = "buGUngi ob-Havo Qanday ekaN"
print(txt22.swapcase())  # BUguNGI OB-hAvo qANDAY EKAn

txt23 = "Hamma keldi bugun"
txt23_1 = "Hamma keldi bugun"
print(txt23.startswith("Hamma"))  # True
print(txt23_1.startswith("Kim"))  # False

txt24 = "Bugungi darsimiz, kechagi darsimiz"
print(txt24.splitlines())  # ['Bugungi darsimiz, kechagi darsimiz']

txt25 = "I like banana       "
print(txt25.rstrip())  # I like banana

txt26 = "Men har kuni dars qilaman, dars qilish mening hobbiyim"
print(txt26.rpartition("dars"))  # ('Men har kuni dars qilaman, ', 'dars', 'qilish mening hobbiyim')

txt27 = "Har kuni dars qilaman"
print(txt27.rjust(30))  # Har kuni dars qilaman

txt28 = "MENGA OLMA YOQADI"
print(txt28.lower())  # menga olma yoqadi

txt29 = "salom DUNYO"
txt29_1 = "SALOM DUNYO"
print(txt29.isupper())  # False
print(txt29_1.isupper())  # True

txt30 = "   "
txt30_1 = "salom"
print(txt30.isspace())  # True
print(txt30_1.isspace())  # False
