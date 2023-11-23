from ICrud.ImpInterfaceCliente import ImpInterfaceCliente


class ClientControler:
    
    @staticmethod
    def create(**kwargs):
        ImpInterfaceCliente.create(**kwargs)
        
    @staticmethod
    def search(**kwargs):
        return ImpInterfaceCliente.search(**kwargs)    
        
    @staticmethod
    def data(self):
        ...