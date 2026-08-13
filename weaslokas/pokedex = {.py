pokedex = {
    "gible": {"tipo": "dragon", "nivel": 9, "region": "sinnoh"},
    "pikachu": {"tipo": "electrico", "nivel": 25, "region": "kanto"},
    "charmander": {"tipo": "fuego", "nivel": 12, "region": "kanto"}
}

# Acceder directo (sin for) porque el nombre es la clave
print(pokedex["gible"])              # {"tipo": "dragon", "nivel": 9, "region": "sinnoh"}
print(pokedex["gible"]["nivel"])     # 9

# Recorrer todos
for nombre, datos in pokedex.items():
    print(nombre, "->", datos["tipo"], "- nivel", datos["nivel"])