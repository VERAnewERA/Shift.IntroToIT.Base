#INTRO TO IT 2nd COURSE
# Задача 6: Гласные в высоте!
# Посчитай количество гласных букв в строке.
def vowel_count(string):
    return sum(1 for character in string if character.lower() in "aeeeeeeeeee")
string = "Hello, world!"
print(f"In '{string}' {vowel_count(string)} vowels")