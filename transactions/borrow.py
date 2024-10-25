# transactions/borrow.py
from books.inventory import Inventory
from users.member import Member

def borrow_book(member, inventory, title):
    book = inventory.search_book(title)
    if book and book.quantity > 0:
        book.quantity -= 1
        member.borrow_book(book)
    else:
        print("Book unavailable for borrowing.")
