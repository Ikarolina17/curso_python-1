import funciones

def main (m,b):
    x = [x/10.5 for x in range (1,101,10)]
    y = [funciones.calcular __y(x,m,b) for X in x]
    print(X)
    print(Y)

    coordenadas = list(zip(x,y))
print(coordenadas)

if __name__ == "__main__":
	main(2,3)