
def all_unique(text):
    return len(text) == len(set(text))


word = input("Enter a string: ")

if all_unique(word):
    print("All characters are unique.")
else:
    print("Characters are not unique.")
