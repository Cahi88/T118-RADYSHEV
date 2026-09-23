def count_words(text):
    return len(text.split())
text = input("введите строку")
print(("кол-во слов"),count_words(text))