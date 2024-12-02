import doctest


# TODO Написать 3 класса с документацией и аннотацией типов
class Book:  # Абстрактный класс для описания книги.
    def __init__(self, title: str, author: str, page_count: int):
        """
        Создание и подготовка к работе объекта "Книга"

        :param title: Название книги.
        :param author: Автор книги.
        :param page_count: Количество страниц.
        :raises ValueError: Если количество страниц меньше или равно 0.

        Примеры:
        >>> book = Book("Граф Монте-Кристо", "Александр Дюма", 1243) # Инициализация экземпляра класса
        """
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Название книги должно быть непустой строкой.")
        if not isinstance(author, str) or not author.strip():
            raise ValueError("Должен быть указан автор книги.")
        if not isinstance(page_count, int) or page_count <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом.")
        self.title = title
        self.author = author
        self.page_count = page_count

    def read(self, page_count_read: int) -> None:
        """
        Чтение книги.

        :param page_count_read: Количество страниц для чтения.
        :raises ValueError: Если количество страниц больше оставшихся в книге.

        Примеры:
        >>> book = Book("Граф Монте-Кристо", "Александр Дюма", 1243)
        >>> book.read(10)
        """
        if not 0 <= page_count_read <= self.page_count:
            raise ValueError("Страниц для чтения не может быть больше, чем есть в книге.")
        ...

    def bookmark(self, page: int) -> None:
        """
        Закладка на страницу.

        :param page: Номер страницы.
        :raises ValueError: Если страница выходит за пределы книги.

        Примеры:
        >>> book = Book("Граф Монте-Кристо", "Александр Дюма", 1243)
        >>> book.bookmark(150)
        """
        if not 0 <= page <= self.page_count:
            raise ValueError("Страница с закладкой выходит за пределы книги.")
        ...

    def get_remaining_pages(self, pages_read: int) -> None:
        """
        Информация о количестве оставшихся непрочитанных страниц.

        :param pages_read: Прочитанные страницы.
        :raises ValueError: Если прочитанных страниц больше оставшихся в книге.
        :return: Количество оставшихся страниц.

        Примеры:
        >>> book = Book("Граф Монте-Кристо", "Александр Дюма", 1243)
        >>> book.get_remaining_pages(100)
        """
        if not 0 <= pages_read <= self.page_count:
            raise ValueError("Прочитанных страниц не может быть больше, чем есть в книге.")
        ...


class Car:  # Абстрактный класс для описания автомобиля.
    def __init__(self, brand: str, model: str, fuel_capacity: float):
        """
        Создание и подготовка к работе объекта "Автомобиль"

        :param brand: Производитель автомобиля.
        :param model: Модель автомобиля.
        :param fuel_capacity: Объем топливного бака в литрах.
        :raises ValueError: Если объем топливного бака меньше или равен 0.

        Примеры:
        >>> car = Car("Ford", "Mustang", 60.0)
        """
        if not isinstance(brand, str) or not brand.strip():
            raise ValueError("Производитель должен быть непустой строкой.")
        if not isinstance(model, str) or not model.strip():
            raise ValueError("Модель должна быть непустой строкой.")
        if not isinstance(fuel_capacity, (int, float)) or fuel_capacity <= 0:
            raise ValueError("Объем топливного бака должен быть положительным числом.")
        self.brand = brand
        self.model = model
        self.fuel_capacity = fuel_capacity

    def drive(self, distance: float) -> None:
        """
        Поездка на определенное расстояние.

        :param distance: Расстояние в километрах.
        :raises ValueError: Если недостаточно топлива.

        Примеры:
        >>> car = Car("Ford", "Mustang", 60.0)
        >>> car.drive(50)
        """
        ...

    def refuel(self, fuel_quantity: float) -> None:
        """
        Заправка автомобиля.

        :param fuel_quantity: Количество топлива.
        :raises ValueError: Если объем топлива превышает вместимость бака.

        Примеры:
        >>> car = Car("Ford", "Mustang", 60.0)
        >>> car.refuel(20.0)
        """
        ...

    def get_fuel_efficiency(self, distance: float, fuel_used: float) -> None:
        """
        Рассчет топливной эффективности автомобиля.

        :param distance: Пройденное расстояние в километрах.
        :param fuel_used: Использованное количество топлива в литрах.
        :raises ValueError: Если расстояние или объем топлива меньше или равен нулю.
        :return: Расход топлива в литрах на 100 км.

        Примеры:
        >>> car = Car("Ford", "Mustang", 60.0)
        >>> car.get_fuel_efficiency(600, 60)
        """
        if distance <= 0 or fuel_used <= 0:
            raise ValueError("Расстояние и объем топлива должны быть больше нуля.")
        if fuel_used > self.fuel_capacity:
            raise ValueError("Использованное топливо не может превышать объем топливного бака.")
        ...


class CloudStorage:  # Абстрактный класс для описания облачного хранилища.
    def __init__(self, name: str, storage_capacity: float, security_level: str = ""):
        """
        Создание и подготовка к работе объекта "Облачное хранилище"

        :param name: Название хранилища.
        :param storage_capacity: Объем доступного хранилища в гигабайтах.
        :param security_level: Уровень защиты данных (standard, high).
        :raises ValueError: Если объем хранилища меньше или равен 0.
        :raises ValueError: Если уровень защиты данных указан некорректно.

        Примеры:
        >>> cloud = CloudStorage("MyCloud", 100.0, "Standard")
        """
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Название должно быть непустой строкой.")
        if not isinstance(storage_capacity, (int, float)) or storage_capacity <= 0:
            raise ValueError("Объем хранилища должен быть положительным числом.")
        if security_level not in ["Standard", "High"]:
            raise ValueError("Уровень защиты должен быть 'Standard' или 'High'.")
        self.name = name
        self.storage_capacity = storage_capacity
        self.security_level = security_level

    def upload_file(self, file_size: float) -> None:
        """
        Загрузка файла в хранилище.

        :param file_size: Размер файла в гигабайтах.
        :raises ValueError: Если объем файла превышает доступное место.

        Примеры:
        >>> cloud = CloudStorage("MyCloud", 100.0, "Standard")
        >>> cloud.upload_file(10.0)
        """
        ...

    def delete_file(self, file_size: float) -> None:
        """
        Удаление файла из хранилища.

        :param file_size: Размер файла в гигабайтах.

        Примеры:
        >>> cloud = CloudStorage("MyCloud", 100.0, "Standard")
        >>> cloud.delete_file(5.0)
        """
        ...

    def increase_security_level(self) -> None:
        """
        Повышение уровня защиты данных до следующего.

        :raises ValueError: Если уровень защиты уже находится на максимальном уровне.

        Примеры:
        >>> cloud = CloudStorage("MyCloud", 100.0, "Standard")
        >>> cloud.increase_security_level()
        >>> cloud.security_level
        'High'
        """
        if self.security_level == "Standard":
            self.security_level = "High"
        elif self.security_level == "High":
            raise ValueError("Уровень защиты уже максимальный.")
        else:
            raise ValueError("Неверный текущий уровень защиты.")
        ...


if __name__ == "__main__":  # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()  # Тестирование doctest-примеров
