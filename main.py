import json

# Accessing an attribute
# data["items"][index][key]

# Dict hard-mapping gold efficiency values
# Measure in X gold per point
goldEfficiency = {
    "AttackDamage": 35,
    "AbilityHaste": 50,
    "AbilityPower": 20,
    "Armor": 20,
    "MagicResist": 18,
    "Health": 2.67,
    "Mana": 1.4,
    "HealthRegen": 3,
    "ManaRegen": 5,
    "CritChance": 40,
    "AttackSpeed": 25,
    "FlatMovespeed": 12,
    "LifeSteal": 53.57,
    "PercentArmorPen": 41.67,
    "FlatMagicPen": 31.11,
    "PercentMagicPen": 46.15,
    "OnHit": 21.67,
    "PercentMovespeed": 80,
    "HealAndShieldPower": 68.75
}

# sorc 45MS * 12

with open("./items.json") as file:
    data = json.load(file)


# Gives the percent efficiency of each item based on its stats
def is_efficient(statsGold, item):
    return round((statsGold / item["price"]) * 100, 2)

# Identifies the ratio of gold per stat allocated for each item
def find_ratio(item):
    statsGold = 0
    for key in goldEfficiency:
        if key in item["stats"]:
            statsGold += round(item["stats"].get(key) * goldEfficiency.get(key), 2)

    return statsGold


for i in range(len(data["items"])):
    currItem = data["items"][i]
    print(currItem["name"])
    print(is_efficient(find_ratio(currItem), currItem), "% efficiency")