class Library():

    def __init__(self,list):
        self.all_books = list
        self.available_books = list
        self.lend_books = {}

    def display_available_books(self):
        for book in self.available_books:
            print(book)

    def display_all_books_list(self):
        for book in self.all_books:
            print(book)

    def display_lend_books(self,name,book):
        if book not in self.all_books:
            print("please eneter the proper book")
            return
        if book in self.available_books:
            self.lend_books.update({book:name})
            self.available_books.remove(book)
            print("you can take the book")
        else:
            print("this book is taken by" + self.lend_books[book])

    def display_return_book(self,book):
        del self.lend_books[book]
        self.available_books.append(book)






if __name__ == "__main__":
    lib = Library(["book1", "book2", "book3", "book4", "book5"])
    print("welcome to the Library Enter the option")
    while True:
        print("Display Available book please enter 1")
        print("Display all books please enter 2")
        print("book edukanum please enetr 3")
        print("book ah return pannanum please enetr 4")
        print("Quit Please enter 5")
        value = int(input())
        if value == 1:
            lib.display_available_books()
        elif value == 2:
            lib.display_all_books_list()
        elif value ==3:
            name = input("please enter the name")
            book = input("please enetr the book")
            lib.display_lend_books(name,book)
        elif value ==4:
            book = input("please enter the name of the book")
            lib.display_return_book(book)
        if value == 5:
            break

