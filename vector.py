import time
import numpy as np

inicio = time.time()
#Suma vectorizada usando vectorización de numpy
# np.arange crea la secuencia de números ddesde 0 a 1499999
print(np.sum(np.arange(1500000)))
fin = time.time()
print(fin - inicio)

#1124999250000
#0.0025 segundos