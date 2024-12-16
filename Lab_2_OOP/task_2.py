BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:  # TODO написать класс Book
    def __init__(self, id_: int, name: str, pages: int):
        """
        Инициализация книги.

        :param id_: Идентификатор книги.
        :param name: Название книги.
        :param pages: Количество страниц в книге.
        """
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        """
        Возвращает строковое представление книги для пользователя.
        """
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """
        Возвращает строку, которая позволяет инициализировать точно такой же объект.
        """
        return f"Book(id_={self.id}, name={repr(self.name)}, pages={self.pages})"


class Library:  # TODO написать класс Library
    def __init__(self, books=None):
        """
        Инициализация библиотеки.

        :param books: Список книг (необязательный аргумент, по умолчанию пустой список).
        """
        self.books = books if books is not None else []

    def get_next_book_id(self) -> int:
        """
        Возвращает идентификатор для добавления новой книги.
        Если книг нет, возвращает 1.
        Если книги есть, возвращает идентификатор последней книги увеличенный на 1.
        """
        if not self.books:
            return 1
        return max(book.id for book in self.books) + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """
        Возвращает индекс книги в списке по её id.

        :param book_id: Идентификатор книги.
        :raises ValueError: Если книги с указанным id нет в библиотеке.
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    # Проверяем библиотеку с пустым списком
    empty_library = Library()  # Инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # 1

    # Создаём список книг из базы данных
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]

    # Проверяем библиотеку с книгами
    library_with_books = Library(books=list_books)  # Инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # Проверяем следующий id для непустой библиотеки
    print(library_with_books.get_index_by_book_id(1))  # Проверяем индекс книги с id = 1

    # # Проверка ошибки, если книга не найдена
    # try:
    #     print(library_with_books.get_index_by_book_id(5))  # Ошибка
    # except ValueError as e:
    #     print(e)  # Книги с запрашиваемым id не существует
