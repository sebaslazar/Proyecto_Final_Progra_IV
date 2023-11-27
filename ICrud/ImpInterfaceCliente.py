from Model import Cliente as cliente, CrudModels, ICrud

class ImpInterfaceCliente(ICrud.ICrud):
    
    def create(**kwargs):
        new_client = cliente.Cliente(**kwargs)
        CrudModels.CrudModels.clients.append(new_client)
        return new_client
        # print(CrudModels.CrudModels.clients)
        
    def append_bill(**kwargs):
        client = kwargs["client"]
        client.bills = kwargs["bill"]
        
    def search(**kwargs):
        for client in CrudModels.CrudModels.clients:
            if client.dni == kwargs["dni"]:
                return client
            
        return False
    
    def data(**kwargs):            
        ...