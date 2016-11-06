"""
Nombre: Rodriguez Bocanegra, Juan Daniel
Materia: Seminario de Solucion de Problemas de Estrcturas de Datos II
Profesor: Armida Vazquez

Actividad 01, 02, 03
"""

import os
import sys
import string
import time

class nodoEmpleados():
    def __init__(self,data):
        self.pos = data[0]
        self.key = data[1]

class AdminEmpleados():
    def __init__(self):
        self.lista = []
        self.nCampos = ["\tNo de nomina: ", "\tApellidos: ","\tNombre(s): ",\
            "\tTelefono: ","\tPuesto: ","\tNSS: ","\tDomicilio: "]

    def leerIndice(self):
        try:
            with open ("i_empleados.txt",'r') as f:
                self.lista.clear()
                for linea in f:
                    i = 0
                    while linea [i] != '|':
                        i += 1
                    pos = int(linea[0:i])
                    key = linea[i+1:len(linea)-1]

                    n = nodoEmpleados([pos,key])
                    self.lista.append(n)
        except FileNotFoundError:
            pass #print("\n\t(!) Error: No se pudo leer el fichero indice")

    def gaurdarIndice(self):

        with open ("i_empleados.txt",'w') as f:
            for n in self.lista:
                f.write(str(n.pos) + '|'+ n.key+'\n')

    def agregar(self):
        self.cadena = ''
        self.campos = []

        print("\n\t...Agregar empleado... ")
        self.campos.append( input ("\n\tIngrese el numero de nomina: ").upper())

        for n in self.lista:
            if  n.key == self.campos[0]:
                print("\n\t(!) Error: Ya existe un registro con este numero de nomina!")
                input("\n\tPresione cualquier tecla para continuar...")
                return


        self.campos.append( input ("\n\tIngrese los apellidos: ").upper())
        self.campos.append( input ("\n\tIngrese los nombres: ").upper())
        self.campos.append( input ("\n\tIngrese el telefono: ").upper())
        self.campos.append( input ("\n\tIngrese el puesto: ").upper())
        self.campos.append( input ("\n\tIngrese el numero de seguro social: ").upper())
        self.campos.append( input ("\n\tIngrese el domicilio: ").upper())

        i = 0
        self.cadena = ''
        while i < len(self.campos):
            if len(self.campos[i]) < 10:
                self.cadena += '0'+str(len(self.campos[i]))+self.campos[i]
                i += 1
            elif len(self.campos[i]) >= 10:
                self.cadena += str(len(self.campos[i]))+self.campos[i]
                i += 1

        f = open ('empleados.txt','a')
        n = nodoEmpleados([str(f.tell()),self.campos[0]])
        self.lista.append(n)

        self.gaurdarIndice()

        f.write(self.cadena+'\n')
        f.close()

    def mostrarTodos(self):
        self.cadena = ''
        tam = 0

        if len(self.lista) < 1:
            input("\n\t(!) No hay registros guardados! \n\n\tPresione <ENTER> para continuar...")
            return

        try:
            print("\n\t...Mostrar todos los registros empleado... \n\n")

            with open ("empleados.txt",'r') as f:
                print ("==============================================")

                for linea in f:
                    i = 0
                    j = 0
                    cadena = linea
                    print("----------------------------------------------")
                    while i+1 < len(cadena):
                        tam = int (cadena[i:i+2])
                        i += 2
                        print ('{0:15} {1:} '.format(self.nCampos[j], cadena[i:i+tam]))
                        j += 1
                        i += tam
                    print("----------------------------------------------")
                print ("==============================================")

        except FileNotFoundError:
            print("\n\t(!) No se encontro el archivo de registros!")
        input("\n\tPresione una tecla para continuar...")

    def buscar(self):
        cadena = ''
        tam = 0
        opc = -1

        if len(self.lista) < 1:
            input("\n\t(!) No hay registros guardados! \n\n\tPresione <ENTER> para continuar...")
            return

        try:
            f = open ('empleados.txt','r')
            while opc != 0:
                print("\n\t...Buscar empleado... \n\n \
                    \n\tDesea buscar por...\n\n\t1.- Numero de nomina\n\t2.- Nombre del empeado\
                    \n\t0.- Salir de la busqueda\n")

                entrada = input("\n\tEscoja una opcion: ")

                while entrada.isdigit() != True:
                    entrada = input("\n\tIngrese una opcion del menu: ")

                opc = int(entrada)
                if opc == 1:
                    flag = False
                    n_busq = input("\n\tIngrese el numero de nomina a buscar: ")
                    for n in self.lista:
                        if n.key == n_busq:
                            print("\n\tEmpleado encontrado!!!")
                            pos = int (n.pos)
                            flag = True
                            i = 0
                            j = 0

                            with open ("empleados.txt",'r') as f:
                                f.seek(pos)
                                cadena = f.readline()
                                print("-----------------------------------------")
                                while i+1 < len(cadena):
                                    tam = int (cadena[i:i+2])
                                    i += 2
                                    print ('{0:15} {1:} '.format(self.nCampos[j], cadena[i:i+tam]))
                                    j += 1
                                    i += tam
                                print("-----------------------------------------")

                    if flag == False:
                        print("\n\tNo se econtro el empleado con el numero de nomina: ",n_busq)

                elif opc == 2:
                    flag = False
                    ape_busq = input("\n\tIngrese los apellidos a buscar: ").upper()
                    nom_busq = input ("\n\tIngrese el nombre a buscar: ").upper()

                    for linea in f:
                        i = 0
                        cadena = linea
                        tam = int(cadena[i:2])
                        i += tam+2
                        tam = int(cadena[i:i+2])
                        i += 2
                        tmp_ape = cadena[i:i+tam]
                        i += tam
                        tam = int(cadena[i:i+2])
                        i += 2
                        tmp_nom = cadena[i:i+tam]

                        if tmp_ape + tmp_nom == ape_busq + nom_busq:
                            print("\n\tEmpleado encontrado!!!")
                            flag = True
                            i = 0
                            j = 0
                            cadena = linea
                            print("-----------------------------------------")
                            while i+1 < len(cadena):
                                tam = int (cadena[i:i+2])
                                i += 2
                                print ('{0:15} {1:} '.format(self.nCampos[j], cadena[i:i+tam]))
                                j += 1
                                i += tam
                            print("-----------------------------------------")

                    if flag == False:
                        print("\n\tNo se econtro el empleado con el nombre: ",nom_busq+" ",ape_busq)

                elif opc == 0:
                    return

            f .close()
        except FileNotFoundError:
            print("\n\t(!) No se encontro el archivo de registros!")
        input("\n\tPresione una tecla para continuar...")

    def modificar(self):
        flag = False
        self.reg_campos = []
        self.cadena = ''
        self.cadenaN = ''

        if len(self.lista) < 1:
            input("\n\t(!) No hay registros guardados! \n\n\tPresione <ENTER> para continuar...")
            return
        try:

            f = open("empleados.txt",'r')
            print("\n\t...Modificar empleado...\n\t")
            n_Nom = input("\n\tIngrese el numero de nomina del empleado a modificar : ").upper()

            for n in self.lista:
                if n.key == n_Nom:
                    flag = True
                    print("\n\tEmpleado encontrado, Numero de nomina: ",n.key,"\n")
                    pos = int (n.pos)
                    f.seek(pos)
                    self.cadena = f.readline()
                    posList = self.lista.index(n)

            f.close()

            if flag == True:
                opc = 'z'

                i = 0
                j = 0
                while i+1 < len(self.cadena):
                    tam = int (self.cadena[i:i+2])
                    i += 2
                    self.reg_campos.append(self.cadena[i:i+tam])
                    j += 1
                    i += tam

                while opc != 0:


                    print('{0:21}{1:}'.format("\n\t1.- Apellidos:",self.reg_campos[1]))
                    print('{0:20}{1:}'.format("\t2.- Nombre(s):",self.reg_campos[2]))
                    print('{0:20}{1:}'.format("\t3.- Telefono:",self.reg_campos[3]))
                    print('{0:20}{1:}'.format("\t4.- Puesto:",self.reg_campos[4]))
                    print('{0:20}{1:}'.format("\t5.- NSS:",self.reg_campos[5]))
                    print('{0:20}{1:}'.format("\t6.- Domicilio:",self.reg_campos[6]))
                    print("\t0.- Salir")
                    opc = input("\n\tSeleccione una opcion para modificar: ")

                    while opc.isdigit() == False:
                        opc =  input ("\n\t(!)Ingrese una de las opciones en pantalla!!\n\t")

                    opc = int(opc)
                    if opc == 1:
                        self.reg_campos.pop(1)
                        tmp = input("\n\tIngrese el nuevo apellido: ").upper()
                        self.reg_campos.insert(1,tmp)
                    elif opc == 2:
                        self.reg_campos.pop(2)
                        tmp = input("\n\tIngrese el/los nuevo(s) nombre(s): ").upper()
                        self.reg_campos.insert(2,tmp)
                    elif opc == 3:
                        self.reg_campos.pop(3)
                        tmp = input("\n\tIngrese el nuevo telefono: ").upper()
                        self.reg_campos.insert(3,tmp)
                    elif opc == 4:
                        self.reg_campos.pop(4)
                        tmp = input("\n\tIngrese el nuevo puesto: ").upper()
                        self.reg_campos.insert(4,tmp)
                    elif opc == 5:
                        self.reg_campos.pop(5)
                        tmp = input("\n\tIngrese el nuevo NSS: ").upper()
                        self.reg_campos.insert(5,tmp)
                    elif opc == 6:
                        self.reg_campos.pop(6)
                        tmp = input("\n\tIngrese el nuevo domicilio: ").upper()
                        self.reg_campos.insert(6,tmp)
                    elif opc == 0:
                        break
                    else:
                        print("\n\t(!) Seleccione una opcion del menu")


                    self.cadenaN = ''
                    i = 0
                    while i < len(self.reg_campos):
                        if len(self.reg_campos[i]) < 10:
                            self.cadenaN += '0'+str(len(self.reg_campos[i]))+self.reg_campos[i]
                            i += 1
                        elif len(self.reg_campos[i]) >= 10:
                            self.cadenaN += str(len(self.reg_campos[i]))+self.reg_campos[i]
                            i += 1

                cont = 0

                with open ("empleadosAux.txt",'w') as aux:
                    with open ("empleados.txt", 'r') as reg:
                        for linea in reg:

                            if cont == posList:
                                self.lista[cont].pos = aux.tell()
                                aux.write(self.cadenaN+'\n')
                            else :
                                self.lista[cont].pos = aux.tell()
                                aux.write(linea)
                            cont += 1

                self.gaurdarIndice()

                os.remove("empleados.txt")
                os.rename("empleadosAux.txt","empleados.txt")
                print("\n\tRegistro actualizado!!!")

            elif flag == False:
                print("\n\t(!) No se encontro el empleado con el numero de nomina: ",n_Nom)

        except FileNotFoundError:
                print("\n\t(!) No se encontro el archivo de registros!")
        input("\n\tPresione una tecla para continuar...")

    def eliminar(self):
        flag = False

        if len(self.lista) < 1:
            input("\n\t(!) No hay registros guardados! \n\n\tPresione <ENTER> para continuar...")
            return
        print("\n\t...Eliminar empleado...")
        n_Nom = input("\n\tIngrese el numero de nomina del empleado que desea borrar: ")

        for n in self.lista:

            if n.key == n_Nom:
                print("\n\tEmpleado encontrado!!!")
                pos = int (n.pos)
                flag = True
                i = 0
                j = 0

                with open ("empleados.txt",'r') as f:
                    f.seek(pos)
                    cadena = f.readline()
                    print("-----------------------------------------")
                    while i+1 < len(cadena):
                        tam = int (cadena[i:i+2])
                        i += 2
                        print ('{0:15} {1:} '.format(self.nCampos[j], cadena[i:i+tam]))
                        j += 1
                        i += tam
                    print("-----------------------------------------")

        if flag == True:
            print("\n\tConfirmar eliminar empleado! \
                \n\t1.- Si \n\t2.- No")
            opc = input("\n\tIngrese una de las opciones: ")
            while opc != '1' and opc != '2':
                opc = input("\n\tIngrese una opcion del menu: ")
            opc = int(opc)
            if opc == 1:

                self.lista.clear()

                regN = open ("empleadosN.txt",'a')
                with open ("empleados.txt",'r') as regO:
                    for linea in regO:
                        i = 0
                        tam = int(linea[i:2])
                        i += 2
                        k = linea[i:i+tam]
                        if k != n_Nom:
                            nodo = nodoEmpleados([str(regN.tell()),k])
                            self.lista.append(nodo)
                            regN.write(linea)

                self.gaurdarIndice()
                os.remove("empleados.txt")
                os.rename("empleadosN.txt","empleados.txt")
                print("\n\tRegistro eliminado exitosamente!!")

            elif opc == 2:
                print("\n\t(!) Eliminacion abortada!!!")

        elif flag == False:
            print("\n\tNo se econtro el empleado con el numero de nomina: ",n_Nom)

        input("\n\tPresione <ENTER> para continuar...")

class MenuEmpleados():
    admin = AdminEmpleados()
    def __init__(self):
        self.datos = []

    op = -1
    while op != 0:
        admin.leerIndice()
        os.system("clear")
        print("\n\tMENU EMPLEADOS \n\n\t1.- Agregar\n\t2.- Mostrar todos los registros\n\t3.- Buscar\
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
            admin.mostrarTodos()
        elif op == 3:
            os.system("clear")
            admin.buscar()
        elif op == 4:
            os.system("clear")
            admin.modificar()
        elif op == 5:
            os.system("clear")
            admin.eliminar()
        elif op == 0:
            exit()
        else:
            print ("\n\t(!) Ingrese una opcion valida!!")
