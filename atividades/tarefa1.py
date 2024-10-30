  #tarefa1
impar=0
par=0
for I in range(10):
    valor=int(input("informe um numero"))
    if(valor%2==0):
        print("o numero e par")
        par=par+1
    else:
      print("numero e impar")
      impar=impar+1