class StringUtility:
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string

    def vowels(self):
        count = sum(1 for char in self.string if char.lower() in 'aeiou')
        return str(count) if count < 5 else 'many'

    def bothEnds(self):
        if len(self.string) <= 2:
            return ''
        else:
            return self.string[:2] + self.string[-2:]

    def fixStart(self):
        if len(self.string) <= 1:
            return self.string
        else:
            first_char = self.string[0]
            return first_char + self.string[1:].replace(first_char, '*')

    def asciiSum(self):
        return sum(ord(char) for char in self.string)

    def cipher(self):
        shift = len(self.string)
        encoded = ''
        for char in self.string:
            if char.isalpha():
                if char.islower():
                    base = ord('a')
                else:
                    base = ord('A')
                encoded_char = chr((ord(char) - base + shift) % 26 + base)
            else:
                encoded_char = char
            encoded += encoded_char
        return encoded
