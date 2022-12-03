from django.shortcuts import render
from . prod import Produit
# Create your views here.
produitsListetab=[{'id':1,'name':'vent','description':'glasse'},{'id':2,'name':'glasse','description':'glasse2'}]
def index(request):
    produit='Mes produits sont'
    # Produits=['produit 1','produit 2','produit3','produit 4']
    Produits=Produit.all()
    return render(request,'vente/index.html',{'produit':produit,'produits':Produits})
def show(request,id):
    produit=Produit.find(id)
    return render(request,'vente/show.html',{'produit':produit})
    
     
