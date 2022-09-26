tipo_pizza = input("Desea una pizza vegetariana? ")
if tipo_pizza == "Si":
    ingrediente = input("Desea pimiento o tofu? ")
    print(f"Su pizza vegetariana con tomate, queso y {ingrediente} esta en camino")
elif tipo_pizza == "No":
    ingrediente = input("Desea pepperoni, jamon o salmon? ")
    print(f"Su pizza no vegetariana con tomate, queso y {ingrediente} esta en camino")
else:
    print("Responda 'Si' o 'No'")