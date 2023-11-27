from ICrud.ImpInterfaceFertilizantes import ImpInterfaceFertilizantes

class FertilizerController:
   
   @staticmethod
   def create(**kwargs):
      return ImpInterfaceFertilizantes.create(**kwargs)
   
   @staticmethod
   def data():
      return ImpInterfaceFertilizantes.data()