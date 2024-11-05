class WordsFinder:
    def __init__(self, *filenames):
        self.file_names = filenames

    def get_all_words(self):
        all_words = {}
        punctuation = [',', '.', '=', '!', '?', ';', ':', '-', '(', ')']

        for filename in self.file_names:
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read().lower()

                for symbol in punctuation:
                    content = content.replace(symbol, '')
                    
                words = content.split()
                all_words[filename] = words

        return all_words

    def find(self, word):
        positions = {}
        all_words = self.get_all_words()

        for filename, words in all_words.items():
            if word.lower() in words:
                index = words.index(word.lower())
                positions[filename] = index + 1

        return positions

    def count(self, word):
        counts = {}
        all_words = self.get_all_words()

        for filename, words in all_words.items():
            count = words.count(word.lower())
            if count > 0:
                counts[filename] = count

        return counts


finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))
