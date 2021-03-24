def get_list(self, fichero):
    lista_palabras=[]
    lista_lon_palabras=[]
    dic_palabras={}
    for i in range(20):
        dic_palabras[i]=" "
    with open(fichero, mode="rt", encoding="utf-8") as f:
        print("dentro de f" +str(f.read(10)))
        texto_vacio=False
        for linea in f:
            aux=linea.split(" ")
            print("aux"+aux)
            for p in aux:
                repetida= linea.count(p)
                lista_lon_palabras.append(len(p))
                lista_palabras.append(p)

    
    for pa in lista_lon_palabras:
        lista_aux=[]
        for j in lista_palabras:
            if pa == len(j):
                lista_aux.append(j)
            dic_palabras[pa]= lista_aux
    #print(dic_palabras)

get_list(self="ra", fichero="frase.txt")