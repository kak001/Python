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

buscar_pirata = input("Ingresa el nombre del pirata: ")

for pirata in recompensas_piratas:
    if pirata[0] == buscar_pirata:
        print(f"Se encontro el pirata: '{buscar_pirata}'")
        break
    
else:
    print((f"No se encontro el nombre del pirata: '{buscar_pirata}'"))
