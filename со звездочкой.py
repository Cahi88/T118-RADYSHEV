def is_palindrome(text)
    return text == text[::-1]
print(is_palindrome("топот"))
print(is_palindrome("python"))