#create a program that takes some text and returns a list of all characters
# in the text that are not vowels, sorte in alphabetical order

text = "the quick brown hare"


vowels = {"a", "e", "i", "u"}

consoants = set()

for letter in text:
    if letter not in vowels and letter != " ":
        consoants.add(letter)

print(sorted(consoants))

#better way

#Strings ARE LISTS!!!
vowels2 = frozenset("aeiou ")

finalSet = set(text).difference(vowels2)

print(sorted(finalSet))