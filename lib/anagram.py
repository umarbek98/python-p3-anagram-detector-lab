class Anagram:
    def __init__(self, word):
        self.word_letters = sorted(letter for letter in word)

    def match(self, word_list):
        match_word = []

        for word in word_list:
            if sorted([letter for letter in word]) == self.word_letters:
                match_word.append(word)

        return match_word
