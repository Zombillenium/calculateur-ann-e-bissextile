 #année bissextile

année = input("vérifiez que l'année est bissextile : ")
print(année)
année = int(année)
div4 = année % 4
div100 = année % 100
div400 = année % 400
if div4 != 0 :
  print("l'année n'est pas bissextile")
elif div100 != 0:
  if div400 != 0:
    print("l'année est bissextile")
  else :
    print("l'année n'est pas bissextile")

  #année bissextile compacte

année = input("vérifiez que l'année est bissextile : ")
année = int(année) 
if année % 400 == 0 or (année % 4 == 0 and année % 100 != 0 ):
  print("l'année est bissextile")
else :
  print("l'année n'est pas bissextile")
