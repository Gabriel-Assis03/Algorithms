def is_palindrome_iterative(word):
    if len(word) == 1:
        return True
    if word == '' or len(word) < 1:
        return False
    if word == ''.join(reversed(word)):
        return True
    return False
