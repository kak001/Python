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

# 1. Separar arreglos: crear piratas y recompensas a partir de recompensas_piratas
piratas = []
recompensas = []

for pirata in recompensas_piratas:
    piratas.append(pirata[0])
    recompensas.append(pirata[1])

print("=== Arreglos separados ===")
print("Piratas:", piratas)
print("Recompensas:", recompensas)

# 2. Pirata más buscado: el de mayor recompensa
recompensa_maxima = max(recompensas)
indice_maximo = recompensas.index(recompensa_maxima)
pirata_mas_buscado = piratas[indice_maximo]

print("\n=== Pirata más buscado ===")
print(f"{pirata_mas_buscado} con una recompensa de {recompensa_maxima} millones de berries")

# 3. Piratas sobre un umbral
umbral = int(input("\nIngresa un umbral de recompensa (en millones): "))

print(f"\n=== Piratas con recompensa mayor a {umbral} millones ===")
for i in range(len(piratas)):
    if recompensas[i] > umbral:
        print(f"{piratas[i]}: {recompensas[i]} millones")

# 4. Resumen de recompensas
total = sum(recompensas)
promedio = total / len(recompensas)

print("\n=== Resumen de recompensas ===")
print(f"Total: {total} millones de berries")
print(f"Promedio: {promedio:.2f} millones de berries")