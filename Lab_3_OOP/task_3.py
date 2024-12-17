class Book:
    """Базовый класс книги."""
    def __init__(self, name: str, author: str):
        self._name = name  # Приватный атрибут "Название" для неизменяемости через свойства
        self._author = author  # Приватный атрибут "Автор" для неизменяемости через свойства

    @property
    def name(self) -> str:
        """Свойство для получения названия книги. Неизменяемо."""
        return self._name

    @property
    def author(self) -> str:
        """Свойство для получения автора книги. Неизменяемо."""
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """Класс для бумажной книги."""
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        """Свойство для получения количества страниц."""
        return self._pages

    @pages.setter
    def pages(self, value: int):
        """Проверка при установке значения для количества страниц."""
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом.")
        self._pages = value

    def __str__(self):
        return f"Бумажная книга {self.name}. Автор {self.author}. Количество страниц: {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"


class AudioBook(Book):
    """Класс для аудиокниги."""
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        """Свойство для получения продолжительности аудиокниги."""
        return self._duration

    @duration.setter
    def duration(self, value: float):
        """Проверка при установке значения для продолжительности аудиокниги."""
        if not isinstance(value, (float, int)) or value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом.")
        self._duration = float(value)

    def __str__(self):
        return f"Аудиокнига {self.name}. Автор {self.author}. Продолжительность: {self.duration:.2f} часов"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"


# Тесты
if __name__ == "__main__":
    paper_book = PaperBook(name="Гарри Поттер", author="Дж. К. Роулинг", pages=500)
    print(paper_book)
    print(repr(paper_book))

    audio_book = AudioBook(name="Хоббит", author="Дж. Р. Р. Толкин", duration=11)
    print(audio_book)
    print(repr(audio_book))

    try:
        paper_book.pages = -100  # Проверка ошибки
    except ValueError as e:
        print(e)

    try:
        audio_book.duration = 0  # Проверка ошибки
    except ValueError as e:
        print(e)
