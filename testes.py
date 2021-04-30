import re

entradaGeneros = str(input("Digite o topX e o gênero: ")).upper().split()

topN = int(re.sub('[^0-9]','', entradaGeneros[0]))

genero = entradaGeneros[1].replace("'", "")

print(type(topN))
print(type(genero))
