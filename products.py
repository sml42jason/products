products = []
while True:
    name = input('Please input name of products : ')
    if name == 'q':
    	break
    price = input('Please input price : ')
    # p = []
    # p.append(name)
    # p,append(price)
    products.append([name, price])
print(products)

for p in products:
	print(p[0],':', p[1])
