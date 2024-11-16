from pprint import pprint

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        symbols = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                line = file.read().lower()
                for i in symbols:
                    line = line.replace(i, '')
                all_words[file_name] = line.split()
        return all_words

    def find(self, word):
        word = word.lower()
        dictionary = {}
        for file_name, words in self.get_all_words().items():
            if word in words:
                dictionary[file_name] = words.index(word) + 1
        return dictionary

    def count(self, word):
        word = word.lower()
        word_counts = {}
        for file_name, words in self.get_all_words().items():
            word_counts[file_name] = words.count(word)
        return word_counts

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего