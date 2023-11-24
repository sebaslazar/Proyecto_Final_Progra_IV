from ICrud.imp_inter_cliente import ImpInterfaceCliente


class ClientControler():
    
    @staticmethod
    def create(**kwargs):
        ImpInterfaceCliente.create(**kwargs)
        
    @staticmethod
    def search(**kwargs):
        return ImpInterfaceCliente.search(**kwargs)    
        
    @staticmethod
    def data(**kwargs):
        ...