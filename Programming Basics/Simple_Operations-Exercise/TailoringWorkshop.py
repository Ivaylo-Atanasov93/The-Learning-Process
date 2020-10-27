tableNumber = int(input())
tableLenght = float(input())
tableWidth = float(input())

tablecloth = (tableLenght + 2*0.30) * (tableWidth + 2*0.30)
quad = (tableLenght / 2) * (tableLenght / 2)

squaremetersOfFabricT = tablecloth * tableNumber
squaremetersOfFabricQ = quad * tableNumber

priceForT = squaremetersOfFabricT * 7
priceForQ = squaremetersOfFabricQ * 9

priceUSD = priceForQ + priceForT

print(f'{priceUSD:.2f} USD')
print(f'{priceUSD*1.85:.2f} BGN')
