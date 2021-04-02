from paradigma import resolver
from matriz import passos

if __name__ == '__main__':
    passo = passos()	
    for item in passo:
        resolver(item)
