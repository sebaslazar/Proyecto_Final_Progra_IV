from ICrud.ImpInterfaceAntibiotico import ImpInterfaceAntibiotico

class AntibioticController:
   
   @staticmethod
   def create(**kwargs):
      return ImpInterfaceAntibiotico.create(**kwargs)