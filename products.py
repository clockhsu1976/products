products = [] #大清單
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入價格名稱:')
	products.append([name, price])
	#p = [name, price] 
	#p = []   #小清單
	#p.append(name)
	#p.append(price)
	#products.append(p)
print(products)
for p in products:
	print(p)

