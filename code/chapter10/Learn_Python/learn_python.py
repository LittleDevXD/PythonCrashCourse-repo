"""with open('learn_python.txt') as file:
    for line in file:
        print(line.rstrip())"""

with open('learn_python.txt') as file:
    lines = file.readlines()
    

text = ''
for line in lines:
    text += line


print(text.replace('python', 'C'))



