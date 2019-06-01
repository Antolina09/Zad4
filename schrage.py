def czytanie_z_pliku(plik_do_wczytania):
    tablica = []
    text_file = open(plik_do_wczytania, "r+")
    for line in text_file.readlines():
         tablica.extend(line.split())
    ilosc_zadan =  int(tablica[0])
    ilosc_maszyn = int(tablica[1])
    index = 2
    zadania_dla_maszyn = [[] for i in range(int(ilosc_maszyn))]
    while index < (ilosc_maszyn*ilosc_zadan +2):
        for k in range(ilosc_maszyn):
            zadania_dla_maszyn[k].append(int(tablica[index]))
            index+=1
    text_file.close()
    return zadania_dla_maszyn

def min_r(r):
    min = r[0]
    indeks = 0
    for i in range(len(r)):
        if r[i] < min:
            min =  r[i]
            indeks = i
    return min, indeks

def max_q(q):
    max = q[0]
    indeks = 0
    for i in range(len(q)):
        if q[i] > max:
            max =  q[i]
            indeks = i
    return max, indeks

def Schrage(zadania):
    cmax = 0
    zadania_gotowe = [[],[],[]]
    zadania_niegotowe = zadania
    t = min_r(zadania_niegotowe[0])[0]

    while zadania_gotowe != [[],[],[]] or zadania_niegotowe != [[],[],[]]:
        while zadania_niegotowe != [[],[],[]] and min_r(zadania_niegotowe[0])[0] <= t:
            indeks1 = min_r(zadania_niegotowe[0])[1]

            zadania_gotowe[0].append(zadania_niegotowe[0][indeks1])
            zadania_gotowe[1].append(zadania_niegotowe[1][indeks1])
            zadania_gotowe[2].append(zadania_niegotowe[2][indeks1])

            zadania_niegotowe[0].pop(indeks1)
            zadania_niegotowe[1].pop(indeks1)
            zadania_niegotowe[2].pop(indeks1)

        if zadania_gotowe == [[],[],[]]: 
            t = min_r(zadania_niegotowe[0])[0] 
        else:
            max_czas, indeks2 = max_q(zadania_gotowe[2])
            t = t + zadania_gotowe[1][indeks2]
            zadania_gotowe[0].pop(indeks2)
            zadania_gotowe[1].pop(indeks2)
            zadania_gotowe[2].pop(indeks2)
            cmax = max(cmax,t+max_czas)
    print(cmax)
    return cmax

def SchragePMTN(zadania):
    cmax = 0
    zadania_gotowe = [[],[],[]]
    zadania_niegotowe = zadania
    t, l = 0, 0 

    while zadania_gotowe != [[],[],[]] or zadania_niegotowe != [[],[],[]]:
        while zadania_niegotowe != [[],[],[]] and min_r(zadania_niegotowe[0])[0] <= t:
            indeks1 = min_r(zadania_niegotowe[0])[1]
            zadania_gotowe[0].append(zadania_niegotowe[0][indeks1])
            zadania_gotowe[1].append(zadania_niegotowe[1][indeks1])
            zadania_gotowe[2].append(zadania_niegotowe[2][indeks1])

            zadania_niegotowe[0].pop(indeks1)
            zadania_niegotowe[1].pop(indeks1)
            zadania_niegotowe[2].pop(indeks1)
            
            if zadania_gotowe[2][-1] > zadania_gotowe[2][l]:
                zadania_gotowe[1][l] = t - zadania_gotowe[0][-1]
                t = zadania_gotowe[0][-1]
                if zadania_gotowe[1][l] > 0:
                    zadania_gotowe[0].append(zadania_gotowe[0][l])
                    zadania_gotowe[1].append(zadania_gotowe[1][l])
                    zadania_gotowe[2].append(zadania_gotowe[2][l])
            
        if zadania_gotowe == [[],[],[]]: 
            t = min_r(zadania_niegotowe[0])[0] 
        else:
            max_czas, indeks2 = max_q(zadania_gotowe[2])
            l = indeks2
            t = t + zadania_gotowe[1][indeks2]
            zadania_gotowe[0].pop(indeks2)
            zadania_gotowe[1].pop(indeks2)
            zadania_gotowe[2].pop(indeks2)
            cmax = max(cmax,t+max_czas)
    print(cmax)
    return cmax

zadania = czytanie_z_pliku("in100.txt")
Schrage(zadania) #1513, 3076, 6416
#SchragePMTN(zadania) #1492, 3070, 6398
