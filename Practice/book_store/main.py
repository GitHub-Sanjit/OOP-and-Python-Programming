def main():
    try:
        ## initialize book list
        book_list = []
        infile = open("theBooksList.txt", "r")
        line = infile.readline()
        while line:
            book_list.append(line.rstrip("\n").split(","))
            line = infile.readline()
        infile.close()

    except FileNotFoundError:
        print("file is not found")
        print("Starting a new book list!")
        book_list = []

    choice = 0
    while choice != 4:
        print("*** Books Manager***")
        print("1) Add a Book")
        print("2) Lookup a Book")
        print("3) Display Book")
        print("4) Quit")
        choice = int(input())

        if choice == 1:
            print("Adding a Book...")
            nBook = input("Enter the name of the books>>>")
            nAuthor = input("Enter the name of the author >>>")
            nPages = input("Enter the number of pages >>>")
            book_list.append([nBook, nAuthor, nPages])

        elif choice == 2:
            print("Looking up for a book ...")
            keyword = input("Enter Search Term: ")
            for book in book_list:
                if keyword in book:
                    print(book)

        elif choice == 3:
            print("Displaying all Books...")
            for i in range(len(book_list)):
                print(book_list[i])

        elif choice == 4:
            print("Quitting Program")
    print("Program Terminated!")

    ### Saving to external text file
    outFile = open("theBooksList.txt", "w")
    for book in book_list:
        outFile.write(",".join(book) + "\n")
    outFile.close()


if __name__ == "__main__":
    main()
