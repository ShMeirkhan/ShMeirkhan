def grams_to_ounces(grams): # Функция для перевода граммов в унции
    ounces = 28.3495231 * grams
    return ounces
grams = int(input())
print(f"{grams} граммов = {grams_to_ounces(grams)} унций")
