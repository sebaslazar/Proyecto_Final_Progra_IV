
class CrudModels:
    __clients = []
    __products = []
    antibiotics = []
    fertilizers = []
    pests = []
    
    @property
    def clients(self):
        return CrudModels.__clients

    @clients.setter
    def clients(self, new_client):
        return CrudModels.clients.append(new_client)
    
    @property
    def products(self):
        return CrudModels.__products
    
    @products.setter
    def products(self, new_product):
        return CrudModels.products.append(new_product)