disk_size_Mb = 1.44
number_of_pages = 100
number_of_strings_per_page = 50
number_of_symbols_per_string = 25
symbol_size_b = 4

# TODO Найдите количество книг, которое можно разместить на дискете
disk_size_b = disk_size_Mb * 1024 * 1024
book_size_b = symbol_size_b * number_of_symbols_per_string * number_of_strings_per_page * number_of_pages
number_of_duplicates_books_on_disk = round(disk_size_b / book_size_b)

print("Количество книг, помещающихся на дискету:", number_of_duplicates_books_on_disk)
