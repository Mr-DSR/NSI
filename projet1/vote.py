from random import randint
tab=[
    {"votants":3273 , 'choix':[1,5,4,2,3]},
    {"votants":2182 , 'choix':[5,1,4,3,2]},
    {"votants":1818 , 'choix':[5,2,1,4,3]},
    {"votants":1636 , 'choix':[5,4,2,1,3]},
    {"votants":727 , 'choix':[5,2,4,3,1]},
    {"votants":364 , 'choix':[5,4,2,3,1]},
]
t=[
   {'a':[1,5,5,5,5,5]},
   {'b':[5,1,2,4,2,4]},
   {'c':[4,4,1,2,4,2]},
   {'d':[2,3,4,1,3,3]},
   {'e':[3,2,3,3,1,1]},
]

def uniquetour():
    v=[0]*len(tab[0]['choix'])
    for i in range(len(tab)):
        ordre=(tab[i]["choix"]) 
        for j in range(len(ordre)):
            if ordre[j]==1:
                v[j]=tab[i]["votants"]


