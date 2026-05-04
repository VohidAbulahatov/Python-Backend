#string metodlar
#ma'lum obyekt, klassga tegishli funksiya metod deyiladi!
from fnmatch import translate

#t= "katta harifga o'tkaz"
#t2=t.capitalize() #o'zgartirmaydi yangi yaratadi
#print(t2)

#casefold()  hammasini kichik harfga o'tkazadi!

#txt="Hammasini KiChiK HaRfga o'tkaz"
#x= txt.casefold()
#print(x)

#txt.center barchasini markazga olib keladi

#txt="10ta"
#s= txt.center(10)
#print(s)

#count() element qiymatini ber!

#txt="faqat,: bitta : elementni top"
#s= txt.count(":")
#print(s)

#endswith() oxiri nima bilan tugasa shu belgini qaytaradi!

#txt="misolni tugashiga etibor beramiz"
#f= txt.endswith(z)
#print(f)

#txt.expantabse orada joy tashlaydi!

#txt="D/i/l/y/o/r/b/ek"
#txt.expandtabs(4)
#print(txt)

#txt.find boshlanish sanaydi!

#txt="dilyorbek"
#s= txt.find("dilyorbek")
#print(s)

#index boshlanish sanaydi finddan farqi yo'q narsa yozilganda xato beradi!

#txt="yo'q narsa yozib bo'lmaydi"
#x= txt.index("narsa")
#print(x)

#isalnum ichida harf yoki son bo'lsa true qaytaradi!

#txt= "harfva1994sonberaman"
#x = txt.isalnum()
#print(x)

#join tuplni stringga yig'ib beradi!

#x= "-".join(mytuple)
#print(x)

#split ajratib beradi

#txt= "Andijongaa,xush,kelibsiz"
#x= txt.split("a")
#print(x)

#srip boshidagi va oxiridagi bo'sh joylarni kesadi!

#txt= "  hacker   "
#x= txt.strip()
#print(x)

#string ajratadi belgi qoyadi!
#print(x)

#translate() asci javalidan foydalanib harflarni almashtiradi!

#mydict= {83: 115}
#txt= "Salom DunyO"
#print(txt.translate(mydict))

#str.maketrans() jadvaldan foylanilmaydi!

#txt= "Salom DunYO"
#mytable= str.maketrans("S","D","Y")
#print(txt.translate(mytable))
