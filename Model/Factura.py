from datetime import datetime


class Factura:

    def __init__(self) -> None:
        self.__date = datetime.now()
        self.__products = []

    @property
    def date(self):
        return datetime.strftime(self.__date, "%d/%m/%Y, %H:%M:%S")

    @property
    def products(self):
        return self.__products

    @products.setter
    def products(self, new_object):
        self.__products.append(new_object)

    def check_in(self, value):
        self.products.append(value)

    def total_value(self):
        total = 0
        for article in self.products:
            total += article.value
        return total
