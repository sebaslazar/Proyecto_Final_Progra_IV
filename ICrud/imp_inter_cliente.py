from Model import Cliente as cliente, CrudModels, ICrud

class ImpInterfaceCliente(ICrud.ICrud):
    
    def create(**kwargs):
        new_client = cliente.Cliente(**kwargs)
        CrudModels.CrudModels.clients = new_client
        
    def search(**kwargs):
        for client in CrudModels.CrudModels.clients:
            print(vars(client))
            if vars(client) == kwargs:
                return client
            
        return False
    
    def data(**kwargs):            
        ...