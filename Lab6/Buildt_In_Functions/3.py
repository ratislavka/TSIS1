
s = input()

palindrome = False
reversedS = s[::-1]

if s == reversedS:
    palindrome = True

if palindrome:
    print('The string is a palindrome')
else:
    print('The string is not a palindrome')
