def vowelator(word):
    vowels = ["a", "e", "i", "o", "u"] 
    new_word = ""
    for chr in word:
        if chr not in vowels:
            new_word += chr
    print(new_word)

vowelator(input("Enter a word: "))
