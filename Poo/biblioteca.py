class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.avaible = True
    def borrow(self):
        if self.avaible:
            self.avaible = False
            print(f"El libro {self.title} ha sido prestado")
        else:
            print(f"El libro {self.title} no está disponible")
    
    def return_book(self):
        self.avaible = True
        print(f"El libro {self.title} ha sido devuelto ")

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.avaible:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f"El libro{book.title} No está disponible")
    def return_book(self,book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f"El libro {book.title} No está en la lista de prestados")

class Library:
    def __init__(self):
        self.books = []
        self.users = []
    
    def add_books(self,book):
        self.books.append(book)
        print(f"el libro{book.title} ha sido agregado")
    
    def register_user(self,user):
        self.users.append(user)
        print(f"El usuario {user.name} ha sido registrado")
    
    def show_avaible_books(self):
        print("Los libros disponibles son:")
        for book in self.books:
            if book.avaible:
                print(f"{book.title} por {book.author}")


#Crear los libros
book1 = Book("El principito", "Antoine de Saint")
book2 = Book("1984", "George Orwell")

#Crear un usuario 
user1 = User("Laura", "001")

# Crear biblioteca
library= Library()
library.add_books(book1)
library.add_books(book2)
library.register_user(user1)


#Mostrar libros
library.show_avaible_books()

#Realizar prestamo
user1.borrow_book(book1)

#Mostrar libros
library.show_avaible_books()

#Devolver libro
user1.borrow_book(book1)

library.show_avaible_books()
