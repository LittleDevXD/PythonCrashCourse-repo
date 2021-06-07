def count(file):
    try:
        with open(file, encoding='utf-8') as f:
            lines = f.read()
    except FileNotFoundError:
        pass
    else:
        words = lines.split()
        print(f"The file {file} has {len(words)} words.")

count('six_frightened_man.txt')
count('the_dark_road.txt')
