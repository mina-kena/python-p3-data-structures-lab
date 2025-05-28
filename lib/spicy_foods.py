def get_names(spicy_foods):
    names = []
    for food in spicy_foods:
        names.append(food["name"])
    return names

def get_names(spicy_foods):
    names = []
    for food in spicy_foods:
        names.append(food["name"])
    return names

spicy_foods = [
    {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9},
    {"name": "Bufallo Wings", "cuisine": "American", "heat_level": 3},
    {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6}
]

print(get_names(spicy_foods))



