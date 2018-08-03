import re


class Hyphenation:
    WELCOME_MESSAGE: str = 'Welcome to the application'

    def __init__(self, config: dict):
        self.data_file = config.get('data_file')

        with open(self.data_file, 'rt') as file:
            self.data_list = [line.strip() for line in file.readlines()]
            # print(self.data_list)

    def run(self):
        print(Hyphenation.WELCOME_MESSAGE)
        # word = input('Type in the word for hyphenation: ').strip()
        self.hyphenate()

    def hyphenate(self):
        word = input('Type in the word for hyphenation: ').strip()
        letters = list(word)

        for i, val in enumerate(letters):
            if i % 2 == 0:
                letters.insert(i, '0')
        letters.pop(0)

        # pattern without dots and numbers
        clean_patterns = []
        for pattern in self.data_list:
            matched = re.fullmatch(r'(\.\w+)|(\w+)|(\w+\.)', pattern)
            if matched:
                pattern = re.sub(r'[\.\d+]|[\d+\.$]', '', pattern)
                clean_patterns.append(pattern)

        # create a dictionary for 'patterns': 'clean_patterns'
        patterns_dict = dict(zip(self.data_list, clean_patterns))

        for key, value in patterns_dict.items():
            # find the beginning of the word
            if word.startswith(value) and key[0] == '.':
                # print(key)
                for char in key:
                    if char.isdigit():
                        letters[key.find(char) + 1] = char

            # find matches between beginning and the end
            elif value in word and key[0] != '.' and key[-1] != '.':
                # print(key)
                value_position = word.find(value)
                for char in key:
                    if char.isdigit():
                        if key[0] is char:
                            if letters[value_position * 2 - 1] < char:
                                letters[value_position * 2 - 1] = char
                            else:
                                letters[value_position * 2 - 1] = char
                        else:
                            letters[value_position * 2 + 1] = char

            # find the end of the word
            elif word.endswith(value) and key[-1] == '.':
                # print(key)
                value_position = word.find(value)
                for char in key:
                    if char.isdigit():
                        if letters[value_position * 2 - 1].isdigit():
                            if letters[value_position * 2 - 1] < char:
                                letters[value_position * 2 - 1] = char
                        else:
                            letters.insert(value_position * 2 - 1, char)

        for char in letters:
            if char.isdigit() and int(char) % 2 == 0:
                letters.remove(char)

        word_with_odds = ''.join(letters)
        hyphenated_word = ''
        for char in word_with_odds:
            if char.isdigit() and int(char) % 2 != 0:
                hyphenated_word = word_with_odds.replace(char, '-')
                word_with_odds = hyphenated_word

        print('Hyphenated word: ', hyphenated_word)
