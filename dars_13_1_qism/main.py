# def my_is_digit(my_str):
#     sanoq = 0
#     yigindi = 0
#     for i in my_str:
#         if i.isdigit():
#             sanoq += 1
#             yigindi += int(i)
#     return (sanoq, yigindi)
#
#
# print(my_is_digit("Myname123isvohid"))


# misol
# def wor_with_list(a):
#
#
#     m = min(a)
#     a1 = []
#     for i in a:
#         a1.append(i * m)
#     return a1
# print(wor_with_list([2,4,6]))

# misol
# def expensive_product(products):
#     max_price = 0
#     max_product = {}
#     for i in products:
#         if i["price"] > max_price:
#             max_price = i["price"]
#             max_product = i
#     return max_product["name"]
#
#
# arr = [
#     {
#         "name": "Iphone X",
#         "price": 600
#     },
#     {
#         "name": "Iphone 12",
#         "price": 1500
#     },
#     {
#         "name": "Samsung Note 9",
#         "price": 800
#     },
#     {
#         "name": "Samsung S10",
#         "price": 1100
#     },
# ]
# print(expensive_product(arr))


# misol
# def min_max(number, max_num, min_num):
#     min1 = min(number)
#     max1 = max(number)
#     if max1 == max_num:
#         print("Maximumni togri topdingiz")
#     else:
#         print("Maximum xato")
#     if min1 == min_num:
#         print("Minimumni togri topdingiz")
#     else:
#         print("Minimum xato")
# min_max([22,23,43,54,14,76,74,98],98,14)


# misol:
def kpi_function(soatbay, summa):
    jami = soatbay * summa
    return jami


maosh = kpi_function(120, 50000)
print(f"Sizning bu oydagi KPI maoshingiz: {maosh} ")
