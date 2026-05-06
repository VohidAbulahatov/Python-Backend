tehnikalar = ["samsung", "apple", "xiomi"]
tehnikalar.append("huawei")
print(tehnikalar)  # ['samsung', 'apple', 'xiomi', 'huawei']

tehnikalar2 = ["apple", "samsung"]
tehnikalar2_1 = ["lg", "xiomi"]
x = tehnikalar2.extend(tehnikalar2_1)
print(tehnikalar2)  # ['apple', 'samsung', 'lg', 'xiomi']

tehnikalar3 = ["samsung", "apple", "xiomi", "lg"]
tehnikalar3.insert(3, "windows")
print(tehnikalar3)  # ['samsung', 'apple', 'xiomi', 'windows', 'lg']

tehnikalar4 = ["samsung", "apple", "xiomi", "lg"]
tehnikalar4.pop(2)
print(tehnikalar4)  # ['samsung', 'apple', 'lg']

tehnikalar5 = ["samsung", "apple", "xiomi", "lg"]
tehnikalar5.remove("apple")
print(tehnikalar5)  # ['samsung', 'xiomi', 'lg']

tehnikalar6 = ["samsung", "apple", "lg"]
tehnikalar6.clear()
print(tehnikalar6)  # []

tehnikalar7 = ["samsung", "apple", "xiomi", "lg"]
x1 = tehnikalar7.copy()
print(x1)  # ['samsung', 'apple', 'xiomi', 'lg']

tehnikalar8 = ["apple", "samsung", "xiomi", "lg", "apple"]
x3 = tehnikalar8.count("apple")
print(x3)  # 2

tehnikalar9 = ["apple", "samsung", "xiomi", "lg", "apple"]
x4 = tehnikalar9.index("lg")
print(x4)  # 3

tehnikalar10 = ["apple", "samsung", "xiomi", "lg"]
tehnikalar10.sort(reverse=True)
print(tehnikalar10)  # ['xiomi', 'samsung', 'lg', 'apple']

tehnikalar11 = ["apple", "samsung", "xiomi", "lg"]
tehnikalar11.sort(reverse=False)
print(tehnikalar11)  # ['apple', 'lg', 'samsung', 'xiomi']

tehnikalar12 = ["apple", "samsung", "xiomi", "lg"]
tehnikalar12.reverse()
print(tehnikalar12)  # ['lg', 'xiomi', 'samsung', 'apple']
