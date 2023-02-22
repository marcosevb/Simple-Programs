class Authors:
    def __init__(self, author_id, first_name, last_name, country, birth_date):
        self.author_id = author_id
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.birth_date = birth_date

class Books:
    def __init__(self, book_id, title, ISBN, publication_date, publisher_id):
        self.book_id = book_id
        self.title = title
        self.ISBN = ISBN
        self.publication_date = publication_date
        self.publisher_id = publisher_id

class Publishers:
    def __init__(self, publisher_id, name, country, website):
        self.publisher_id = publisher_id
        self.name = name
        self.country = country
        self.website = website

class BookAuthors:
    def __init__(self, book_id, author_id):
        self.book_id = book_id
        self.author_id = author_id

class Members:
    def __init__(self, member_id, first_name, last_name, email, address):
        self.member_id = member_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.address = address

class Loans:
    def __init__(self, loan_id, book_id, member_id, loan_date, return_date):
        self.loan_id = loan_id
        self.book_id = book_id
        self.member_id = member_id
        self.loan_date = loan_date
        self.return_date = return_date


# Create 5 objects for the Authors table
author1 = Authors(1, "Jane", "Doe", "USA", "1980-01-01")
author2 = Authors(2, "John", "Smith", "Canada", "1985-02-02")
author3 = Authors(3, "William", "Johnson", "UK", "1990-03-03")
author4 = Authors(4, "Emily", "Brown", "Australia", "1995-04-04")
author5 = Authors(5, "Michael", "Davis", "New Zealand", "2000-05-05")

# Create 5 objects for the Books table
book1 = Books(1, "Book1", "ISBN1", "2021-01-01", 1)
book2 = Books(2, "Book2", "ISBN2", "2022-02-02", 2)
book3 = Books(3, "Book3", "ISBN3", "2023-03-03", 3)
book4 = Books(4, "Book4", "ISBN4", "2024-04-04", 4)
book5 = Books(5, "Book5", "ISBN5", "2025-05-05", 5)

# Create 5 objects for the Publishers table
publisher1 = Publishers(1, "Publisher1", "USA", "www.publisher1.com")
publisher2 = Publishers(2, "Publisher2", "Canada", "www.publisher2.com")
publisher3 = Publishers(3, "Publisher3", "UK", "www.publisher3.com")
publisher4 = Publishers(4, "Publisher4", "Australia", "www.publisher4.com")
publisher5 = Publishers(5, "Publisher5", "New Zealand", "www.publisher5.com")

# Create 10 objects for the BookAuthors table
book_author1 = BookAuthors(1, 1)
book_author2 = BookAuthors(2, 2) 
book_author3 = BookAuthors(3, 3)
book_author4 = BookAuthors(4, 4)
book_author5 = BookAuthors(5, 5) 
book_author6 = BookAuthors(1, 5)
book_author7 = BookAuthors(2, 4)
book_author8 = BookAuthors(3, 3)
book_author9 = BookAuthors(4, 2)
book_author10 = BookAuthors(5, 1)

# Put objects for the Authors table into a list
authors = [author1, author2, author3, author4, author5]

# Put objects for the Books table into a list
books = [book1, book2, book3, book4, book5]

# Put objects for the Publishers table into a list
publishers = [publisher1, publisher2, publisher3, publisher4, publisher5]

# Put objects for the BookAuthors table into a list
book_authors = [book_author1, book_author2, book_author3, book_author4, book_author5, 
                book_author6, book_author7, book_author8, book_author9, book_author10]

""" 1)	list all publisher's names and websites. """
def Question1():
    print ("\nAll Publishers' Names and Websites:")
    for p in publishers:
        print( p.name + " - " + p.website)

Question1()

""" 2)	List all book's book_id published by publisher Publisher1. """
def Question2():
    for b in books:
        if b.publisher_id == 1:
            print("\nBook_IDs published by Publisher1: " + str(b.book_id) + "\n")

Question2()

"""3)	find the author_id of author Jane Doe, where Jane is the author's first name and Doe is her last name. """
def Question3():
    for a in authors:
        if a.first_name == "Jane" and a.last_name == "Doe":
            return (a.author_id)

print("Author ID of Jane Doe: " + str(Question3()) + "\n")

"""4)	(use the result from question 3), find all books' book_id authored by Jane Doe. """
def Question4():
    janeDoeAuthorID = Question3() #get results from Q3 and declare new list for books by jane doe
    booksByJaneDoe = [];

    for ba in book_authors:
        if ba.author_id == janeDoeAuthorID:
            booksByJaneDoe.append(ba.book_id)

    return booksByJaneDoe #return list which contains all books by jane doe

print("Book_IDs of books authored by Jane Doe: " + str(Question4()) + "\n")

"""5)	(use the result from question 3 and 4), find Jane Doe's coauthors' first_name and last _name. coauthors can be found by writing a same book but with different author_id. """
def Question5():
    janeDoeAuthorID = Question3() #get results from Q3, Q4, and declare new list for coauthors
    booksByJaneDoe = Question4()
    CoAuthoredWithJD = []

    for bjd in booksByJaneDoe: #find coauthors and add them to a list
        for b in book_authors:
            if (b.book_id == bjd and b.author_id != janeDoeAuthorID):
                CoAuthoredWithJD.append(b.author_id);

    CoAuthoredWithJD = list(set(CoAuthoredWithJD)) #this converts the list into a set and then back into a list, in order to remove the duplicates

    print("Jane Doe's CoAuthors:")
    for ca in CoAuthoredWithJD: #print first and last name of coauthors
        for a in authors:
            if a.author_id == ca:
                print(a.first_name + " " + a.last_name)

Question5() 

"""6)	find author's author_id who has published more than one book."""
def Question6():
    print("\nAuthors' IDs who have published more than one book:")

    for a in authors:
        counter = 0
        for b in book_authors:
            if a.author_id == b.author_id:
                counter = counter + 1
        
        if counter > 1:
            print(str(a.author_id))
    
    print("\n")

Question6() 
