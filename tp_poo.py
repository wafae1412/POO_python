from abc import ABC ,abstractmethod
from dataclasses import dataclass, field
from typing import List

class Boisson(ABC):
    @abstractmethod
    def cout(self):
        pass
    @abstractmethod
    def description(self):
        pass
    def __add__(self,other):
        return BoissonCombine(self,other)
    

class BoissonCombine(Boisson):
    def __init__(self,boisson1,boisson2):
        self._boisson1=boisson1
        self._boisson2=boisson2
    def cout(self):
        return self._boisson1.cout()+self._boisson2.cout()
    def description(self):
        return self._boisson1.description()+" et "+self._boisson2.description()   


@dataclass
class Client:
    nom:str
    numero:int
    points_fidelite:int

    def commander(self,boisson):
        print(f"commande: {boisson.description()}  \n prix : {boisson.cout()} euros")



class Cafe(Boisson):
    def cout(self):
        return 2.0
    def description(self):
        return "café simple"
    
class The(Boisson):
    def cout(self):
        return 1.5
    def description(self):
        return "thé"
    def __repr__(self):
        return f"The()"
   

class DecorateurBoisson(Boisson):
    def __init__(self,boisson):
        self._boisson=boisson

class Lait(DecorateurBoisson):
    def cout(self):
        return self._boisson.cout()+0.5
    def description(self):
        return self._boisson.description()+" ,lait"
    
class Sucre(DecorateurBoisson):
    def cout(self):
        return self._boisson.cout()+0.2
    def description(self):
        return self._boisson.description()+", sucre"

class Caramel(DecorateurBoisson):
    def cout(self):
        return self._boisson.cout()+0.5
    def description(self):
        return self._boisson.description()+", caramel"
    
@dataclass
class Commande:
    client:Client
    boissons: List[Boisson] = field(default_factory=list)
    
    def ajouter_boisson(self,b):
        self.boissons.append(b)
    def total_prix(self):
        total=0
        for b in self.boissons:
            total+=b.cout()
        return total
    def afficher_commande(self):
    
        for b in self.boissons:
            print(f"{b.description()} prix:{b.cout()} euros")
        
        print(f" prix total: {self.total_prix()} euros")
    

class CommandeSurPlace(Commande):
    def __init__(self,client):
        super().__init__(client)
    def ajouter_boisson(self, b):
        super().ajouter_boisson(b)
        print(f"boisson {b.description()} est bien ajouté a la commande sur place du client : {self.client.nom}")
    def total_prix(self):
        total=super().total_prix()
        print(f"le prix total de la commande sur place du client {self.client.nom}est {total} euros")
        return total
    def afficher_commande(self):
        print(f"commande sur place du client:{self.client.nom}:")
        super().afficher_commande()

class CommandeEmporter(Commande):
    def __init__(self,client):
        super().__init__(client)
    def ajouter_boisson(self, b):
        super().ajouter_boisson(b)
        print(f"boisson {b.description()} est  bien ajouté a la commande Emporté du client : {self.client.nom}")
    def total_prix(self):
        total=super().total_prix()
        print(f"le prix total de la commande emporter du client  est {self.client.nom}est {total} euros")
        return total
    def afficher_commande(self):
        print(f"commande emporter du client:{self.client.nom}:")
        super().afficher_commande()

class Fidelite:
    def ajouter_points(self,client,montant):
        points=int(montant)
        client.points_fidelite+=points

class CommandeFidele(Commande,Fidelite):
    def valider_commande(self):
        total=self.total_prix()
        self.ajouter_points(self.client,total)
        
    


#creation du client
client1=Client("wafae",1233345,5)
#creation des boissons
boisson1=Cafe()
boisson1=Lait(boisson1)
boisson1=Sucre(boisson1)
boisson2=The()
boisson3=boisson1+boisson2
boisson4=Cafe()
boisson4=Caramel(boisson4)
#creation de la commande
commande1 = CommandeFidele(client1)
commande1.ajouter_boisson(boisson1)
commande1.ajouter_boisson(boisson2)
commande1.ajouter_boisson(boisson3)
commande1.ajouter_boisson(boisson4)
#affichage de la commande
commande1.afficher_commande()
#validation de la commande
commande1.valider_commande()
#affichage du points de fedilite:
print(f"les points de fedelite de {client1.nom} sont :{client1.points_fidelite}")# ca va afficher 15 car le client a deja 5 points et elle va gangner 10 points de plus pour son achat de 10 euros




