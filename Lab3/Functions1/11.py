
string = input()

'''
def is_palindrome(string):
    if string == string[::-1]:
        return True
    return False
'''

def is_palindrome(string):
    if string == ''.join(reversed(string)):     #The reversed function returns a reverse iterator, not a string. We need to join the characters together to form a reversed string.
        return True
    return False

print(is_palindrome(string))