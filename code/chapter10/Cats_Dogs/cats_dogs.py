class File:
    def __init__(self, file):
        self.file = file

    def write_file(self, text=""):
            with open(self.file, "a") as f:
                f.write(f"- {text}\n")

    def read_file(self):
        try:
            with open(self.file, "r") as f:
                lines = f.read()
                print(self.file)
                print(lines.rstrip()) 
        except FileNotFoundError:
            print(f"File {self.file} does not exist.")

dog = File('dogs.txt')
cat = File('cats.txt')

#dog.write_file('Malamute')
#dog.write_file('Husky')
#dog.write_file('Retriever')

#cat.write_file('Burma')
#cat.write_file('meow')
#cat.write_file('Innlay')

dog.read_file()
cat.read_file()