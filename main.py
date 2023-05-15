llista=[]
opcion=0
while opcion!=5:
  print('1 - Mostra llista')  
  print('2 - Afegeix un nom a la llista: ')  
  print('3 - Escriu un nom:')  
  print('4 - Esborra llista')
  opcion=int(input('Tria una opcio: '))
  
  if opcion==1:
    print(llista)
    
  elif opcion==2:
   nom = input('Escriu un nom: ')
   if not nom in llista:
    llista.append(nom)
  
  elif opcion==3:
    elteunom= input('Esborra el nom: ')
    if elteunom in llista:
       llista.remove (elteunom)
  
    elif opcion==4:
      llista.clear()