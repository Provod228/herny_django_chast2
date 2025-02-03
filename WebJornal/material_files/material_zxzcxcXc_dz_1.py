class Human:
    count = 0

    def __new__(cls, name: str = " ", surname: str = " ", age: int = 0):
        cls.count += 1
        instance = super().__new__(cls)
        instance.__name = name
        instance.__surname = surname
        instance.__age = age
        return instance

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def surname(self) -> str:
        return self.__surname

    @surname.setter
    def surname(self, surname: str) -> None:
        self.__surname = surname

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, age: int) -> None:
        self.__age = age

    @staticmethod
    def get_info(name, surname, age):
        return name, surname, age

    def geter_info(self):
        return self.get_info(self.name, self.surname, self.age)
