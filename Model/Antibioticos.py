class Antibioticos:

    def __init__(self, name, dose, animal_type, value) -> None:
        self.__name = name
        self.__dose = dose
        self.__animal_type = animal_type
        self.__value = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, antibiotic_name):
        self.__name = antibiotic_name

    @property
    def dose(self):
        return self.__dose

    @dose.setter
    def dose(self, antibiotic_dose):
        self.__dose = antibiotic_dose

    @property
    def animal_type(self):
        return self.__animal_type

    @animal_type.setter
    def animal_type(self, kind):
        self.__animal_type = kind

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, cost):
        self.__value = cost

    def __str__(self) -> str:
        info = f"NOMBRE: {self.name}\tDOSIS: {self.dose}\n"
        info += f"VALOR: {self.value}\tTIPO DE ANIMAL: {self.animal_type}"
        return info
