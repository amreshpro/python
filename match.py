#  switch -> match


# vowel or not
# char = input("Enter the character: ")

def checkVowel(c):
    match c:
        case 'A' | 'a':
            return "Yes"
        case 'E' | 'e':
            return "Yes"
        case 'I' | 'i':
            return "Yes"
        case 'O' | 'o':
            return "Yes"
        case 'U' | 'u':
            return "Yes"
        case _:
            return "No"


print(checkVowel("a"))
print(checkVowel("s"))
