def is_palindrome(s):
    # функция, которая проверяет, является ли строка палиндромом
    s = s.replace(" ", "").lower()
    # удаляем пробелы и приводим к нижнему регистру
    return s == s[::-1]
example=input()
word = "madam"
phrase = "A man a plan a canal Panama"
print(is_palindrome(word))  # Output: True
print(is_palindrome(phrase))  # Output: True
print(is_palindrome(example))