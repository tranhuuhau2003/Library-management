# main.py
from books.book import Book
from books.inventory import Inventory
from users.member import Member
from transactions.borrow import borrow_book
from transactions.return_book import return_book  # Đổi tên import để phù hợp với tên file mới

# Tạo các đối tượng ban đầu
inventory = Inventory()
member1 = Member("Alice", "M001")

# Thêm sách vào kho
book1 = Book("Python Programming", "John Doe", "ISBN123", 3)
book2 = Book("Data Science", "Jane Doe", "ISBN456", 2)
inventory.add_book(book1)
inventory.add_book(book2)

# Mượn sách
borrow_book(member1, inventory, "Python Programming")
borrow_book(member1, inventory, "Data Science")

# Kiểm tra sách còn lại
print("\nCurrent Inventory:")
for book in inventory.books: 
    print(book)

# Trả sách
return_book(member1, inventory, "Python Programming")

# Kiểm tra sách sau khi trả
print("\nUpdated Inventory:")
for book in inventory.books:
    print(book)
