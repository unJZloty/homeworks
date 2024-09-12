def all_variants(text):
    for l in range(1, len(text) + 1):
        for j in range(len(text) - l + 1):
            yield text[j:j + l]

# Пример использования
a = all_variants("abc")
for i in a:
    print(i)