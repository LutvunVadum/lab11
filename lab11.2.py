import json

enterprises_data = [
    {
        "name": "Agroland",
        "land_area": 1500, 
        "annual_profit": 12000 
    },
    {
        "name": "Earth and Ko",
        "land_area": 2000,
        "annual_profit": 17000
    },
    {
        "name": "Silgospprom",
        "land_area": 800,
        "annual_profit": 16000
    }
]

with open('enterprises.json', 'w') as json_file:
    json.dump(enterprises_data, json_file, ensure_ascii=False, indent=4)

print("Файл enterprises.json створено.")

def calculate_efficiency(enterprise):
    area = enterprise['land_area']
    profit = enterprise['annual_profit']
    return profit / area if area > 0 else 0

with open('enterprises.json', 'r') as json_file:
    enterprises = json.load(json_file)

most_efficient = max(enterprises, key=calculate_efficiency)

with open('effect.txt', 'w') as effect_file:
    json.dump(most_efficient, effect_file, ensure_ascii=False, indent=4)

print("Дані про найбільш ефективне підприємство записані у файл effect.txt.")

