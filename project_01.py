
text = input("Enter a sentence or paragraph: ")

# Remove extra spaces
text = " ".join(text.split())

print("\n--- Text Analyzer System ---")

# Count characters, words and sentences
print("Total characters:", len(text))
words = text.split()
print("Total words:", len(words))

sentences = text.count(".") + text.count("!") + text.count("?")
print("Total sentences:", sentences)

# Count vowels, consonants, digits and special characters
vowels = 0
consonants = 0
digits = 0
special = 0

for ch in text:
    if ch.lower() in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    elif not ch.isspace():
        special += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Special characters:", special)

# Convert text
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())

# Search for a word
search_word = input("\nEnter a word to search: ")

if search_word.lower() in text.lower().split():
    print("Word exists in the text")
else:
    print("Word does not exist in the text")

# Find frequency of each word
print("\nWord Frequencies:")
for word in set(text.lower().split()):
    print(word, ":", text.lower().split().count(word))

# Display text after removing extra spaces
print("\nText without extra spaces:", text)
