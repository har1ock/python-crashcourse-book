
def words_count2(filename):

    try:
        with open(filename, encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        repeat = content.lower().count(word)
        print(f"In the file {filename} the word '{word}' has repeated {repeat} times.")


word = input("Введіть слово для перевірки на кількість повторів в тексті, наприклад 'the' :")
filenames = ['white_fang.txt', 'blue_castle.txt', 'romeo_and_juliet.txt',
             'little_women.txt']
for filename in filenames:
    words_count2(filename)
