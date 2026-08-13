recompensas_piratas = [
	["Monkey D. Luffy", 3000],
	["Roronoa Zoro", 1200],
	["Sanji", 1100],
	["Nami", 366],
	["Usopp", 200],
	["Nico Robin", 930],
	["Franky", 500],
	["Brook", 383],
	["Jinbe", 1100],
	["Shanks", 4000],
	["Marshall D. Teach", 3960],
	["Charlotte Linlin", 4388],
	["Kaido", 4611],
	["Buggy", 3189],
	["Trafalgar D. Water Law", 3000],
	["Eustass Kid", 3000]
]

piratas = []
recompensas = []

for pirata in recompensas_piratas:
    piratas.append(pirata[0])
    recompensas.append(pirata[1])

recompensa_max = max(recompensas)
indice_max = recompensas.index(recompensa_max)
pirata_max_buscado = piratas[indice_max]

print("=" * 5, "PIRATA MAS BUSCADO", "=" * 5)
print(f"Nombre: '{pirata_max_buscado}'")
print(f"Recompensa: '{recompensa_max}'")
print("=" * 30)

umbral = int(input("Ingresa un umbral: "))

for i in range(len(piratas)):
    if recompensas[i] > umbral:
        print(f"{piratas[i]}: {recompensas[i]} millones")

total = sum(recompensas)
promedio = total / len(recompensas)

print("=" * 5, "TOTAL Y PROMEDIO DE RECOMPENSAS", "=" * 5)
print(f"Monto total de recompensas: {total}")
print(f"Promedio de recompensas: {promedio}")
print("=" * 43)