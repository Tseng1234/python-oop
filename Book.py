class Book():
    def __init__(self,title,author,ISBN) :
        self.title=title
        self.author=author
        self.ISBN=ISBN
        self.state=False
    def display(self):
        print("title: ",self.title)
        print("author: ",self.author)
        print("ISBN: ",self.ISBN)
        print("State:", "Borrowed" if self.state else "Available")
        print("-------------------------------")
class Library():
    def __init__(self) :
        self.books=[]
    def add_book(self,book):
        self.books.append(book)
    def search_book(self,ISBN):
        for book in self.books:
            if ISBN==book.ISBN:
                book.display()
    def borrow_book(self,ISBN):
        for book in self.books:
            if ISBN==book.ISBN:
                book.state=True
    def return_book(self,ISBN):
        for book in self.books:
            if ISBN==book.ISBN:
                book.state=False
# 建立書籍實例
book1 = Book("Python Crash Course", "Eric Matthes", "9781593279288")
book2 = Book("Clean Code", "Robert C. Martin", "9780132350884")

# 建立圖書館實例
library = Library()

# 新增書籍到圖書館
library.add_book(book1)
library.add_book(book2)

# 查詢書籍
library.search_book("9781593279288")

# 借出書籍
library.borrow_book("9781593279288")

# 再次查詢書籍
library.search_book("9781593279288")

# 歸還書籍
library.return_book("9781593279288")

# 再次查詢書籍
library.search_book("9781593279288")

