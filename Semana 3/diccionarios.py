elegir = input("Enter a currency (Euro, Dollar or Yen): ")
billete = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
print(billete.get(elegir.title(), "Currency doesn't exist"))