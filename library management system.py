class Library():
    def __init__(self,List,name):
        self.booklist = List
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f" books available in our Library:")
        for book in self.booklist:
            print(book)

    def lendBook(self,user,book):
        if book not in self.lendDict.keys():
            self.booklist.remove(book)
            print("you can take the book")
        else:
            print("book is not available .")

    def addBook(self,book):
        self.booklist.append(book)
        print("book has been added")


    def returnBook(self,book):
        self.lendDict.pop(book)
        self.booklist.append(book)
        print("Your book have been sucessfully returned")


if(__name__ == "__main__"):
    a1 = Library(["python","java","c++","dbms"],"GyanCenter")
    while(True):
        print(f"Welcome to {a1.name}. \n what you want to do?")
        print("1. Display Books Available")
        print("2. Lend Books")
        print("3. Add book in library")
        print("4. Return Book")
        choice = input()
        if choice not in ["1","2","3","4"]:
            continue
        else:
            choice = int(choice)

        if choice == 1:
            a1.displayBooks()

        elif choice == 2:
            book = input("Enter the name of the book you want to lend: ")
            user = input("Enter your name: ")
            a1.lendBook(user,book)

        elif choice == 3:
            book = input("Enter the name of the book you want to add: ")
            a1.addBook(book)

        elif choice == 4:
            book = input("Enter the name of the book you want to return: ")
            a1.returnBook(book)

        else:
            print("invaid input")


        print("press Q to Quit and C to Continue")
        newchoice = ""
        while(newchoice != "c" and newchoice != "q"):
            newchoice = input()
            if newchoice == "Q":
                exit()
            if newchoice == "C":
                continue
