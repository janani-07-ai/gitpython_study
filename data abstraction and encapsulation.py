#  Data abstraction and Encapsulation

class library():
    def __init__(self,books):
        self.books=books
    def list_books(self):
        print("Available books are: ")
        for books in self.books:
            print(books)
    def borrow_book(self,borrow_book):
        if borrow_book in self.books:
            print("get the book")
            self.books.remove(borrow_book)
        else:
            print("sorry,book is not available")
    def received_book(self,received_book):
        print("enter the book you return:")
        self.books.append(received_book)
books=['java','c++','python']
object=library(books)
msg="""
1. get availability
2. borrow books
3. return books
"""
print(msg)
while True:
    ch=int(input("enter the choice:"))
    if ch==1:
        object.list_books()
    elif ch==2:
        books=input("enter the book to borrow:")
        object.borrow_book(books)
    elif ch==3:
        books=input("enter the book to return:")
        object.received_book(books)
    else:
        print("thank you come again!!!")
        quit()

        