from Model import Factura, CrudModels, ICrud
from datetime import date, datetime

class ImpInterfaceFactura(ICrud.ICrud):
    
    def create(**kwargs):
        return Factura.Factura(**kwargs)
    
    def append_products(**kwargs):
        bill = kwargs["bill"]
        for product in kwargs["products"]:
            bill.products = product
    
    def search(**kwargs):
        delivered_date = kwargs["date"]
        for bill in kwargs["bills"]:
            if bill.date == delivered_date:
                return bill
            
        return False
    