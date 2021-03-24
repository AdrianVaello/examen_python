from libro import Libro
from autor import Autor

def get_list(self, fichero):
    lista_palabras=[]
    lista_lon_palabras=[]
    dic_palabras={}
    for i in range(20):
        dic_palabras[i]=" "
    with open(fichero, mode="rt", encoding="utf-8") as f:
        for linea in f:
            aux=linea.split(" ")
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
    print(dic_palabras)

get_list(self="ra", fichero="frase.txt")

#-------------------------------------
l1= Libro(autor=Autor(id_autor="1",nombre="Adrian", apellido="Vaello"),titulo="Las leyendas de pepe",anyo=2021)
l2= Libro(autor=Autor(id_autor="2",nombre="Nacho", apellido="kajs"),titulo="Las historias de aroon",anyo=2014)
l3= Libro(autor=Autor(id_autor="3",nombre="Stephen", apellido="Vaello"),titulo="Harry potter",anyo=1978)
lista_libros=[]
lista_libros.append(l1)
lista_libros.append(l2)
lista_libros.append(l3)

def mas_antiguos(self, libros, ano):
    for l in libros:
        

mas_antiguos(self="sf",libros=lista_libros,ano=2000)