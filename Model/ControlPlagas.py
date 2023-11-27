from Model import ProductosControl as producto_control


class ControlPlagas(producto_control.ProductosControl):

    def __init__(self, ica, name, freq, value, grace_period):
        self.__grace_period = grace_period
        super().__init__(ica, name, freq, value)

    @property
    def grace_period(self):
        return self.__grace_period

    @grace_period.setter
    def grace_period(self, period):
        self.__grace_period = period

    def __str__(self) -> str:
        info = f"ICA: {self.ica}\tNOMBRE: {self.name}\tFRECUENCIA: {self.freq}\n"
        info += f"VALOR: {self.value} \PERIODO DE CARENCIA: {self.grace_period}"
        return info

    def __dict__(self):
        local_vars = {
            "type": "Pests",
            "name": self.name,
            "ica": self.ica,
            "freq": self.freq,
            "grace_period": self.grace_period,
            "value": self.value
        }
        return local_vars
    
    __dict__ = property(__dict__)