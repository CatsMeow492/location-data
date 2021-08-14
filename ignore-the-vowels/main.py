word = str(input())
vowels = ["a", "e", "i", "o", "u"]


def anti_vowel(word):
    chars = []
    for letter in word: #No need of the two separate loops
        if letter not in vowels:
            chars.append(letter)
        

    print(chars)

anti_vowel(word)