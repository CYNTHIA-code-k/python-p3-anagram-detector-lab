# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()
        self.sorted_word = sorted(self.word)

    def match(self, candidates):
        return [
            candidate for candidate in candidates
            if self.is_anagram(candidate)
        ]

    def is_anagram(self, candidate):
        candidate = candidate.lower()
        return (
            candidate != self.word and
            sorted(candidate) == self.sorted_word
        )