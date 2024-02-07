string = input()

def reverse_words(string):
    words = string.split()
    reverse = ' '.join(reversed(words))
    return reverse
print(reverse_words(string))
