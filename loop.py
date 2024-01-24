import time
inicio = time.time()
#suma iterativa 
total = 0 
#iteracion a travez 1.5  millones de números
for item in range(0, 1500000):
    total = total + item

print(' la suma es:' + str(total))
fin = time.time()
print(fin - inicio)
#1124999250000
#0.1021509 segundos
