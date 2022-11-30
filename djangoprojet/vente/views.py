from django.shortcuts import render

# Create your views here.
produitsListetab=[{id:1,'name':'vent','description':'glasse'},{id:2,'name':'glasse','description':'glasse2'}]
def index(request):
    produit='Mon produit3'
    Produits=['produit 1','produit 2','produit3','produit 4']
    return render(request,'vente/index.html',{'produit':produit,'produits':Produits})
def show(request,id):
    produit=produitsListetab[id -1]
    return render(request,'vente/show.html',{'produit':produit})
    
     
