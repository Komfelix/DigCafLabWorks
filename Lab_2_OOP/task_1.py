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


if __name__ == "__main__":
    # Инициализация списка книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]

    # Проверяем метод __str__
    for book in list_books:
        print(book)

    # Проверяем метод __repr__
    print(list_books)
