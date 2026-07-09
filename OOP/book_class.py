class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print(f"{self.title} by {self.author}")

b1 = Book("A Suitable Boy", "Vikram Seth")
b1.display()
