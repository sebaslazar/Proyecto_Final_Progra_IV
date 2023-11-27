from ICrud.ImpInterfaceFertilizantes import ImpInterfaceFertilizantes

class FertilizerController:
   
   @staticmethod
   def create(**kwargs):
      return ImpInterfaceFertilizantes.create(**kwargs)