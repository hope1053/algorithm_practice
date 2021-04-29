n = int(input())
books = list()
book_count = list()
for _ in range(n):
    books.append(input())

book_set = set(books)
for book in book_set:
    book_count.append([books.count(book), book])
book_count.sort(key = lambda x:(-x[0],x[1]))
print(book_count[0][1])