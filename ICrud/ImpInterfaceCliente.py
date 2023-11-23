from ICrud import ICrud
from Model import Cliente, CrudModels

class ImpInterfaceClient(ICrud):
    
    def create(self, **kwargs):
        new_client = Cliente.Cliente(**kwargs)
        CrudModels.CrudModels.clients = new_client
        
    def search(self, **kwargs):
        for client in CrudModels.CrudModels.clients:
            print(vars(client))
            if vars(client) == kwargs:
                return client
            
        return False
    
    def data(self):            
        ...