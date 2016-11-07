"""
Nombre: Rodriguez Bocanegra, Juan Daniel
Materia: Seminario de Solucion de Problemas de Estrcturas de Datos II
Profesor: Armida Vazquez

Entrega 03, del 29 octubre al 05 de noviembre
Descripcion: Implementar Las funciones, agregar(), mostrartodo(), buscar()
modificar() y eliminar(), utilizando registro con delimitadores

id_solicitud
id_cliente
completado(0 = en espera, 1 completado)
auto(por placa)
tipo de servicio(venta, reparacion, mantenimiento, revision)
descripcion
detalles (condiciones del aunto cuando llega)
fecha de recepcion:
fecha compromiso de entrega:
"""
import os
import time
#import sys  #para los formatos
class SolicitudServicio():
    def __init__(self,data):
        self.id_solicitud = data
        self.id_cliente = data
        self.completado = data
        self.placa = data
        self.t_servicio = data
        self.t_descripcion = data
        self.detalles = data
        self.f_llegada = data
        self.f_compromiso = data

    def __str__(self):
        cad = "\n\t ID solicitud: "+str(self.id_solicitud) +\
              "\n\t ID cliente: "+ str()

        return cad


class MenuSolicitudServicio():
    def __init__(self):
        self.datos = []

    op = -1
    while op != 0:
        os.system("clear")
        print("\n\tMENU SOLICITUD DE SERVICIO \n\n\t1.- Agregar\
        \n\t2.- Mostrartodas las solicitudes\n\t3.- Buscar\
        \n\t4.- Modificar\n\t5.- Eliminar\n\t0.- Salir")

        entrada = input("\n\tIngrese una opcion: ")

        while entrada.isdigit() != True:
            entrada = input("\n\tIngrese una opcion del menu: ")

        op = int (entrada)

        if op == 1:
            os.system("clear")
            pass #admin.agregar()
        elif op == 2:
            os.system("clear")
            pass #admin.mostrarTodos()
        elif op == 3:
            os.system("clear")
            pass #admin.buscar()
        elif op == 4:
            os.system("clear")
            pass #admin.modificar()
        elif op == 5:
            os.system("clear")
            pass #admin.eliminar()
        elif op == 0:
            exit()
        else:
            print ("\n\t(!) Ingrese una opcion valida!!")
