#讀取檔案
products = []
with open('products.csv', 'r', encoding = 'utf-8') as s:
    for line in s:
    	if '商品,價格' in line:
    	    continue 
    	name, price = line.strip().split(',')
    	products.append([name, price])
    print(products)

#寫入檔案
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
