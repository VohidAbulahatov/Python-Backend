# Kickik bir loyiha

products = {
    "Apple": 1000,
    'Milk': 10,
    "Bread": 3
}
print('-' * 40)
print('Online shop | Bizning mahsulotlar')
print('-' * 40)

count = 1
for key, value in products.items():
    print(f"{count}.{key} is ${value:.2f}")
    count += 1
