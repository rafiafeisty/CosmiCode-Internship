class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def write_file(self, content):
        with open(self.filename, 'w') as file:
            file.write(content)
        print("Content written to file.")

    def append_file(self, content):
        with open(self.filename, 'a') as file:
            file.write(content)
        print("Content appended to file.")

    def read_file(self):
        try:
            with open(self.filename, 'r') as file:
                content = file.read()
            print("File Content:")
            print("----------------")
            print(content)
            print("----------------")
        except FileNotFoundError:
            print("File not found.")

fm = FileManager("example.txt")

fm.write_file("This is the first line.\n")

fm.append_file("This is an appended line.\n")

fm.read_file()
