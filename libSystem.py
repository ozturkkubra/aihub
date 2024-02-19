class Library:

    def list_book(self):
        f =  open("books.txt")
        file_content = f.read()
        f.close()
        book_list = file_content.splitlines()
        for book in book_list:
            print(book)

    def add_book(self):

        book_title = input("Enter a Book Title:\n")
        book_author = input("Enter the Book Author:\n")
        first_release = input("Enter the First Release:\n")
        number_of_pages = input("Enter the Number of Pages:\n")

        book = f"{book_title}, {book_author}, {first_release}, {number_of_pages}\n"

        f =  open("books.txt", "a+")
        f.write(book)
        f.close()

    def remove_book(self):

        delete_book_name = input("Which book you want to remove?\n ")

        f = open("books.txt")
        file_content = f.read()
        f.close()
        book_list = file_content.splitlines()

        delete_index = -1
        for i in range(len(book_list)):
            book = book_list[i]
            book_info = book.split(", ")
            if book_info[0] == delete_book_name:
                delete_index = i

        if delete_index != -1:
            book_list.pop(delete_index)
        
        new_file_content = "\n".join(book_list)
        f = open("books.txt", "w")
        f.write(new_file_content + "\n")
        f.close() 



lib = Library()

while True:

    print("***************")
    print("*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("***************")

    choose = input("\nWhat do you want?\n")

    if choose == "1": 
        lib.list_book()

    elif choose == "2":
        lib.add_book()

    elif choose == "3":
        lib.remove_book()

    else:
        print("Invalid Selection !")
        break