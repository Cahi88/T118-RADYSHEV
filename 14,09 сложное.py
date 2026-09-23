def count_word(text, word):
    return text.lower().split().count(word.lower())


text = input("Введите предложение: ")
word = input("Введите слово: ")

print("Количество:", count_word(text, word))
