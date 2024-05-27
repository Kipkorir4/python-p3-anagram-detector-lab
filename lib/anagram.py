class Anagram:
    def __init__(self, word):
        self.word = word.lower()
        self.sorted_word = sorted(self.word)
    
    def match(self, possible_anagrams):
        return [anagram for anagram in possible_anagrams if sorted(anagram.lower()) == self.sorted_word]