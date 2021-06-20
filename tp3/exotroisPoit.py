# Considérons maintenant une deuxième classe appelée TroisPoints ayant les attributs privés de
# type Point : __premier, __deuxieme et __troisieme.
from typing import Any
from exo6 import Point
class TroisPoints:
    
    def __init__(self,premier,deuxieme,troisieme):
        self.__premier=premier
        self.__deuxieme =deuxieme
        self.__troisieme=troisieme
    
    @property
    def premier(self):
        return self.__premier
    @premier.setter
    def premier(self,premier):
        self.__premier=premier
        
    @property
    def deuxieme(self):
        return self.__deuxieme
    @deuxieme.setter
    def deuxieme(self,deuxieme):
        self.__deuxieme=deuxieme
    
    @property
    def troisieme(self):
        return self.__troisieme
    @troisieme.setter
    def troisieme(self,troisieme):
        self.__troisieme=troisieme
# sont alignés si AB = AC + BC, AC = AB + BC ou BC = AC + AB (AB désigne la distance séparant
# le point A du point B, pareillement pour AC et BC).
    def sont_alignes(self):
        distance_p1_p2=self.__premier.calculer_distance(self.__deuxieme)
        distance_p1_p3=self.__premier.calculer_distance(self.__troisieme) 
        distance_p2_p3=self.__deuxieme.calculer_distance(self.__troisieme)
        
        verif=[ distance_p1_p2==distance_p1_p3 + distance_p2_p3, distance_p1_p3==distance_p1_p2 + distance_p2_p3 , distance_p2_p3==distance_p1_p3 + distance_p1_p2]
          
        if any(verif)  :
            return True
        else:
            return False