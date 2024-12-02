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
        if value == 5:
            break

