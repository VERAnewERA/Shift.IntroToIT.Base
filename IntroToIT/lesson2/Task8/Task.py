#INTRO TO IT 2nd COURSE
# Задача 8: Слова, слова, слова!
# Узнай количество слов в предложении.
def word_count(string):
    return len(string.split())
string = "Python is great!"
print(f"In '{line}' {word_count(string)} words")
