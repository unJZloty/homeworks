import string
class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    content = file.read().lower()

                    for punct in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        content = content.replace(punct, '')
                    words = content.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")
                all_words[file_name] = []

        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        word = word.lower()
        result = {}

        for file_name, words in all_words.items():
            if word in words:
                result[file_name] = words.index(word) + 1
            else:
                result[file_name] = None

        return result

    def count(self, word):
        all_words = self.get_all_words()
        word = word.lower()
        result = {}

        for file_name, words in all_words.items():
            result[file_name] = words.count(word)

        return result

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))