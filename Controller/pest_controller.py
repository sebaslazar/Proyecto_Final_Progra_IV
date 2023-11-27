from  ICrud.ImpInterfacePlaga import ImpInterfacePlaga

class PestController:
   
   @staticmethod
   def create(**kwargs):
      return ImpInterfacePlaga.create(**kwargs)
   
   @staticmethod
   def data():
      return ImpInterfacePlaga.data()