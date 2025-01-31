#Trova un numero con più di 5 divisori. Stampa i divisori di ogni numero in input,  se ne ha più di 5 fermati.
#if, range, for , while, liste, variabili
divisori = []
while len(divisori) < 5:
    divisori = []
    n = int(input("Inserisci numero: "))
    for i in range(1,n+1, 1):
        if n % i == 0:
            divisori.append(i) 
    print(divisori)
    



# booleani , strighe, tuple, float, break, pass, continue
