
def imprimir(a):
  print(a)
  return
#imprimir("Hola estoy dentro de la funcion")


def cambiame(lista):
  print("Valores dentro de la funcion antes del cambio ", lista)

  lista[2] = 50
  print("Valores dentro de la funcion despues del cambio ", lista)
  return

lista = [20, 30, 40]

cambiame(lista)

print(lista)

def suma(a, b):
  total = a + b
  return total

suma_total = suma(2, 3)

print(suma_total)
