def convertir(pesos, tasa):
  
  valor_dolar = tasa
  dolares = pesos / valor_dolar
  dolares = round(dolares, 2)
  dolares = str(dolares)
  print("Tienes "+ dolares + " dolares")

a = 0

while a != 1:

  menu = '''
  ***********************************************
  *  Conversor de monedas nacionales a dolares  *
  ***********************************************

  1 - Pesos Colombianos
  2 - Pesos Argentinos
  3 - Pesos Chilenos
  4 - Salir

  Elige una opcion: '''

  opcion = int(input(menu))

  if opcion == 1:
    pesos = float(input("Cuanto Pesos colombianos tienes? "))
    convertir(pesos, 3900)
  elif opcion == 2:
    pesos = float(input("Cuanto Pesos argentinos tienes? "))
    convertir(pesos, 102)
  elif opcion == 3:
    pesos = float(input("Cuanto Pesos chilenos tienes? "))
    convertir(pesos, 750)
  elif opcion == 4:
    a = 1
  else:
    print("Ingresaste una opcion invalida!")
