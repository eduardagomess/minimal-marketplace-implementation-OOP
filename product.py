class Products:

    code_generator = 1

    def __init__(self, name, price):
        self.__code = Products.code_generator
        self.__name = name
        self.__price = price
        Products.code_generator += 1

    @property
    def code(self):
        return self.__code

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    def __str__(self):
        return f'Product code: {self.__code} \n Product name: {self.__name} \n Price: R$ {self.__price}'
