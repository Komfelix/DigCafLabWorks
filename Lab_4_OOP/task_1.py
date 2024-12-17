class Electronics:
    """
    Базовый класс для представления электроники.

    Атрибуты:
    :param brand (str): Бренд устройства.
    :param model (str): Модель устройства.
    :param price (float): Цена устройства.
    """
    def __init__(self, brand: str, model: str, price: float) -> None:
        """
        Инициализация базового класса "Электроника".

        Аргументы:
        brand (str): Бренд устройства.
        model (str): Модель устройства.
        price (float): Цена устройства.
        """
        self.brand = brand
        self.model = model
        self._price = price  # Инкапсуляция цены для ограничения прямого доступа

    def __str__(self) -> str:
        """
        Строковое представление объекта.

        Возвращает:
        str: Описание устройства.
        """
        return f"{self.brand} {self.model} (${self._price})"

    def __repr__(self) -> str:
        """
        Представление объекта для отладки.

        Возвращает:
        str: Информация об устройстве.
        """
        return f"Electronics(brand='{self.brand}', model='{self.model}', price={self._price})"

    def get_price(self) -> float:
        """
        Возвращает цену устройства

        Возвращает:
        float: Цена устройства.
        """
        return self._price

    def set_price(self, new_price: float) -> None:
        """
        Устанавливает новую цену устройства

        Аргументы:
        new_price (float): Новая цена устройства.
        """
        if new_price < 0:
            raise ValueError("Цена не может быть отрицательной.")
        self._price = new_price


class Notebook(Electronics):
    """
    Дочерний класс для представления ноутбуков.

    Атрибуты:
    :param ram (int): Объем оперативной памяти в ГБ.
    :param cpu (str): Модель процессора.
    """

    def __init__(self, brand: str, model: str, price: float, ram: int, cpu: str) -> None:
        """
        Инициализация дочернего класса Laptop.

        Аргументы:
        brand (str): Бренд устройства.
        model (str): Модель устройства.
        price (float): Цена устройства.
        ram (int): Объем оперативной памяти в ГБ.
        cpu (str): Модель процессора.
        """
        super().__init__(brand, model, price)
        self.ram = ram
        self.cpu = cpu

    def __str__(self) -> str:
        """
        Переопределение строкового представления объекта.

        Причина перегрузки: Базовый метод __str__ возвращает минимально необходимую информацию о классе "Электроника".
        Для ноутбуков важно дополнительно отображать технические характеристики, такие как процессор и объем
        оперативной памяти.

        Возвращает:
        str: Расширенное описание ноутбука.
        """
        return f"{self.brand} {self.model} ({self.cpu}, {self.ram}GB RAM) - ${self._price}"

    def upgrade_ram(self, additional_ram: int) -> None:
        """
        Увеличивает объем оперативной памяти

        Аргументы:
        additional_ram (int): Дополнительная память в ГБ.
        """
        if additional_ram <= 0:
            raise ValueError("Объем дополнительной памяти должен быть положительным.")
        self.ram += additional_ram


class Smartphone(Electronics):
    """
    Дочерний класс для представления смартфонов.

    Атрибуты:
    :param camera_mp (int): Разрешение камеры в мегапикселях.
    :param battery_capacity (int): Емкость аккумулятора в мА·ч.
    """

    def __init__(self, brand: str, model: str, price: float, camera_mp: int, battery_capacity: int) -> None:
        """
        Инициализация дочернего класса Smartphone.

        Аргументы:
        brand (str): Бренд устройства.
        model (str): Модель устройства.
        price (float): Цена устройства.
        camera_mp (int): Разрешение камеры.
        battery_capacity (int): Емкость аккумулятора.
        """
        super().__init__(brand, model, price)
        self.camera_mp = camera_mp
        self.battery_capacity = battery_capacity

    def __repr__(self) -> str:
        """
        Переопределение представления объекта для отладки.

        Причина перегрузки: Базовый метод __repr__ возвращает минимально необходимую информацию о классе "Электроника".
        Для смартфонов важно дополнительно отображать технические характеристики, такие как сведения о камере и емкости
        аккумулятора.

        Возвращает:
        str: Расширенная информация о смартфоне.
        """
        return (f"Smartphone(brand='{self.brand}', model='{self.model}', "
                f"price={self._price}, camera_mp={self.camera_mp}, battery_capacity={self.battery_capacity})")

    def take_photo(self) -> str:
        """
        Симуляция съемки фотографии.

        Возвращает:
        str: Сообщение об успешной съемке.
        """
        return f"{self.brand} {self.model} сделал фотографию с разрешением {self.camera_mp} МП."
