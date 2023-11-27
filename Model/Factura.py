from datetime import date


class Factura:

    def __init__(self) -> None:
        self.__date = date.today()
        self.__products = []

    @property
    def date(self):
        
        return date.strftime(self.__date, "%d/%m/%Y")

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
