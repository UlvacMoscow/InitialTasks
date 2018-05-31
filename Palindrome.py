word = 'ollo'


def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False


print(palindrome(word))
