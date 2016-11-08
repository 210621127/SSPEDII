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
from datetime import datetime, date, time, timedelta
import time
#import sys  #para los formatos
class SolicitudServicio():
    def __init__(self,data):
        self.id_solicitud = data
        self.id_cliente = data
        self.placa = data
        self.tipo_servicio = data
        self.descripcion = data
        self.detalles = data
        self.hora = data
        self.f_llegada = data
        self.f_entrega = data
        self.completado = data

    def __str__(self):
        return '{0:23}{1:}'.format("\n\tID solicitud:", str(self.id_solicitud))+\
            '{0:23}{1:}'.format("\n\tID cliente: ", str(self.id_cliente))+\
            '{0:23}{1:}'.format("\n\tPlaca:",str(self.placa))+\
            '{0:23}{1:}'.format("\n\tTipo de servicio:",str(self.descripcion))+\
            '{0:23}{1:}'.format("\n\tDetalles:",str(self.detalles))+\
            '{0:23}{1:}'.format("\n\tHora: ", str(self.hora))+\
            '{0:23}{1:}'.format("\n\tFecha de llegada:",str(self.f_llegada))+\
            '{0:23}{1:}'.format("\n\tFecha compromiso: ",str(self.f_entrega))+\
            '{0:23}{1:}'.format("\n\tCompletado: ",str(self.completado))

class AdminSolicitudServicio():


    def __init__(self):
        self.lista = []
        self.s = SolicitudServicio(None)
        self.t_Servicio = ["Venta","Reparacion","Mantenimiento","Revision"]

    def agregar(self):
        with open("solicitud_servicio.txt",'r') as f:
            self.s.id_solicitud = int(f.readline())

        self.s.id_cliente = input("\n\tID cliente: ")
        self.s.placa = input("\n\tPlaca: ")
        i = 1
        print("\n\tTipo de servicio: ")
        for servicio in self.t_Servicio:
            print ("\t",i,") ",servicio)
            i += 1
        op = input("\n\tSeleccione una opcion: ")
        while True:
            if op == '1' or op == '2' or op == '3' or op == '4':
                break
            else:
                op = input("\t(!) Seleccione una de las opciones anteriores: ")
        self.s.tipo_servicio = self.t_Servicio[int(op)]
        self.s.descripcion = input("\n\tDescripcion del servicio:")
        self.s.detalles = input ("\n\tDetalles del auto: ")

        formato = "%d/%m/%Y"
        ahora = datetime.today()
        self.s.hora = ahora.strftime("%X")
        self.s.f_llegada = ahora.strftime(formato)
        dias = input("\n\tIngrese los dias estimados de entrega: ")
        while dias.isdigit() == False:
            dias = input("\n\t(!) Ingrese solo digitos: ")
        dias = int(dias)
        fechaEntrega = ahora + timedelta(days=dias)
        self.s.f_entrega =  fechaEntrega.strftime(formato)
        self.s.completado = '0';

        print(self.s)
        op = input("\n\tPresione <ENTER> para guardar el registro...")
        ###Aqui me quede en guardar el registro en el archivo .txt



class MenuSolicitudServicio():
    admin = AdminSolicitudServicio()

    def __init__(self):
        pass

    try:
        with open ("solicitud_servicio.txt",'r') as f:
            pass
    except FileNotFoundError:
        print("\n\t(!) No se encontro registro de solicitudes!")
        input("\n\tPresione <ENTER> para crear uno...")
        with open("solicitud_servicio.txt", 'a') as f:
            f.write('0')

    while True:
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
            admin.agregar()
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
