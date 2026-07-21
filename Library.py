import json
class Book :
    def __init__(self, name):
        self.name=name
        self.books= []
    def load(self):
        try:
            with open("library.json", "r") as file:
                self.books = json.load(file)
        except FileNotFoundError:
            print("No saved library found, starting fresh!")


    def options (self):
         
         while True:
            user_ops=input("what do you want :\nadd a book _1\nserche a book _2\nborrowing a book from a library _3\nreturn a book _4\n")


            if user_ops == "1":
                try:
                    user_book = input("what is the name of the book: ").lower()
                    self.books.append(user_book)
                    self.save()
                except:
                    print("Something went wrong")

            elif user_ops == "2":
                search_book = input("what book do you want to search for: ").lower()
                if search_book in self.books:
                    print(f"Yes! '{search_book}' is available.")
                else:
                    print(f"Sorry, '{search_book}' is not available.")

            elif user_ops == "3":
                borrow_book = input("what book do you want to borrow: ")
                if borrow_book in self.books:
                    self.books.remove(borrow_book)
                    self.save()
                    print(f"You borrowed '{borrow_book}'.")
                else:
                    print(f"Sorry, '{borrow_book}' is not available.")

            elif user_ops =="4":
                return_book=input(" what is the book that you want to return it :")
                self.books.append(return_book)
                self.save() 
            else:
                print("there is just four opetions\nplease enter the right opetion that you want")
            again = input("Do you want to do something else? (yes/no) ")
            if again != "yes":
                break
                
    def save(self):
        with open("library.json", "w") as file:
            json.dump(self.books, file)
                
book=Book("City Library")

book.load()

book.options() 

book.save()