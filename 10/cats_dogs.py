"""Вправа 10-8, 10-9"""
def cats_dogs(filename):
    try:
        with open(filename) as f:
            content = f.read()
    except FileNotFoundError:
        # print("File not found")
        pass
    else:
        print(content.strip())


filenames = ['hamster.txt', 'cat.txt', 'dog.txt']
for filename in filenames:
    cats_dogs(filename)
