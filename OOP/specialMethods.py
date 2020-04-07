class Book():

    def __init__(self, name, author, pages):
        super().__init__()
        self.name = name
        self.author = author
        self.pages = pages
    # is called when you call the predefined function print with an instance of this class as parameter 
    def __str__(self):
        return f"{self.name} - {self.author}"
    # is called when you call the predefined python function with an instance of the class

    def __len__(self):
        return int(self.pages)

    def __del__(self):
        print(f"{self.name} has been deleted")


macario = Book(name="Macario", pages="300", author="IDK")
print(macario)
print(len(macario))
del(macario)
