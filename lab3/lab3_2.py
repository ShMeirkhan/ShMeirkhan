def fahrenheit_to_celsius(F):#функция перевода градусов по Фаренгейту в градусы по Цельсию
    celsius = (5 / 9) * (F - 32)
    return celsius
F = int(input())
print(f"{F} градусов по Фаренгейту = {fahrenheit_to_celsius(F)} градусов по Цельсию")