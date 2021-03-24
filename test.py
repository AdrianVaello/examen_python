import unittest
from libro import Libro
from autor import Autor
from examen import mas_antiguos


class Test(unittest.TestCase):
    def set_up(self):
        self.__l1= Libro(autor=Autor(id_autor=1,nombre="Adrian", apellido="Vaello"),titulo="Las leyendas de pepe",anyo=2021)
        self.__l2= Libro(autor=Autor(id_autor=2,nombre="Nacho", apellido="kajs"),titulo="Las historias de aroon",anyo=2014)
        self.__l3= Libro(autor=Autor(id_autor=3,nombre="Stephen", apellido="Vaello"),titulo="Harry potter",anyo=1878)
        self.__lista_libros=[self.__l1,self.__l2,self.__l3]
        self.__masantiguos=mas_antiguos

    def test_mas_antiguos(self):

        self.assertRaises(ValueError,self.__masantiguos, self.__lista_libros, 2000)


if __name__ == '__main__':
    unittest.main()
