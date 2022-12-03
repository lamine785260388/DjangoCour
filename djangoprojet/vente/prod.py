from turtle import stamp

class Produit:
    produits=[
        {'Reférence':50001,'Nom':'confiture de fraise','En stock':'true','prix':23444},
         {'Reférence':50002,'Nom':'confiture de fraise','En stock':'true','prix':23444},
          {'Reférence':50003,'Nom':'confiture de fraise','En stock':'true','prix':23444},
           {'Reférence':50005,'Nom':'confiture de fraise','En stock':'true','prix':23444},
    ]
    @classmethod
    def all(cls):
        return cls.produits
    @classmethod
    def find(self,id):
        return self.produits[id -1]
print(Produit.all())
print(Produit.find(2))