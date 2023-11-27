from ICrud.ImpInterfaceCliente import ImpInterfaceCliente


class ClientControler():
    
    @staticmethod
    def create(**kwargs):
        return ImpInterfaceCliente.create(**kwargs)
        
    @staticmethod
    def append_bill(**kwargs):
        ImpInterfaceCliente.append_bill(**kwargs)
    
        
    @staticmethod
    def search(**kwargs):
        return ImpInterfaceCliente.search(**kwargs)    
        