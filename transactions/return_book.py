# transactions/return.py
from books.inventory import Inventory
from users.member import Member

def return_book(member, inventory, title):
    book = inventory.search_book(title)
    if book:
        book.quantity += 1
        member.return_book(book)
    else:
        print("Book not found in inventory.")
