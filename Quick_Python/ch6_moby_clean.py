# задание на стр 113
# Открыть и прочитать текстовый файл
# Привести к одному регистру
# Удалить знаки препинания
# Разбить на слова
# Записать все слова по одному на строку файла
# outfile.write(cleaned_words)

with open("moby_01.txt") as infile, open("moby_01_clean.txt", "w") as outfile:
    for line in infile:
        pass
