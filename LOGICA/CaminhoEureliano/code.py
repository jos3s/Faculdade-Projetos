from modulos.paradigma import resolver
from modulos.matriz import passos

if __name__ == '__main__':
    passo = passos()
    for item in passo:
        resolver(item)
