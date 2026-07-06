from math import*
import numpy as np 
import matplotlib.pyplot as plt 

# P0 : apport dans le portefeuille
# n : nombre d'année d'investissement
# mensualité : ( oui ou non )
# m : montant des mensualités ( x si oui , 0 si non )
# R : rendement du portefeuille ( ex : 0.03 qui correspond à 3% )

def portefeuille (P0, n , mensualite , m , R): 
  t = np.linspace(1,n,n)
  capital = []
  liquidite = []
  impot = []

  if mensualite == "oui":
    for i in range(1,len(t)+1):

      tot = P0*(1+R)**i + 12*m*(((1+R)**i)-1)/R
      ecart = tot - P0 - m*i*12
      impots= 0.3*ecart # 30% du benefice (total avec intérêts - total sans intérêts )

      capital.append(tot) # Calcul arithmético-géometrique avec mensualité
      liquidite.append(tot - impots)
      impot.append(impots)

  else : 
    for i in range(1,len(t)+1):  # Calcul géométrique sans mensualité
      tot = P0*(1+R)**i
      ecart = tot-P0
      impots= 0.3*ecart
      capital.append(tot)
      liquidite.append (tot-impots)
      impot.append(impots)
    
  taux_zero = [m*12]
  for i in range(n-1):
    taux_zero.append(taux_zero[i]+m*12)


  width = 0.35
  plt.plot(t,taux_zero,'b',label='Capital investis')
  plt.bar(t - width/2, capital, width=width, label='Capital')
  plt.bar(t + width/2, liquidite, width=width, label='Après impôts')
  plt.plot(t,impot,'k',label='Impots')
  plt.title(f"Evolution du capital pour {n} années. \n Avant impots : {capital[-1]:,.2f} €. Après impots : {liquidite[-1]:,.2f} €. \n Avec R={R}, apport={P0}€, mensualité={m}€")
  plt.legend()
  plt.grid(True)
  plt.xlim(0,n+1)
  plt.show()

print(portefeuille(4000,20,"oui",600,0.1))