products = []
while True:
    name = input('Please input name of products : ')
    if name == 'q':
    	break
    price = input('Please input price : ')
    price = int(price)
    # p = []
    # p.append(name)
    # p,append(price)
    products.append([name, price])
print(products)

for p in products:
	print(p[0],':', p[1])

with open('products.csv', 'w', encoding = 'utf-8') as f:
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n')
