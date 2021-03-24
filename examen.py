def get_list(self, fichero):
    lista_palabras=[]
    lista_lon_palabras=[]
    dic_palabras={}
    con=0
    for i in range(20):
        dic_palabras[i]=" "
    with open(fichero, mode="rt", encoding="utf-8") as f:
        for linea in f:
            aux=linea.split(" ")
            #print(aux)
            for p in aux:
                lista_lon_palabras.append(len(p))
                lista_palabras.append(p)
    
    for pa in lista_lon_palabras:
        lista_aux=[]
        for j in lista_palabras:
            if pa == len(j):
                lista_aux.append(j)
            dic_palabras[pa]= lista_aux
        con+=1
    print(dic_palabras)

get_list(self="ra", fichero="frase.txt")