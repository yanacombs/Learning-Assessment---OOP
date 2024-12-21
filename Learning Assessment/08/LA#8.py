class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

book = Book("The Giver", "Lois Lowry")
book2 = Book("It ends with us", "Colleen Hoover")

del book.author
print(book.author)
print(book.title)
print(book2.author)
print(book2.title)
