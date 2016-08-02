import os
import sys
import time
import sqlite3

def menu():
    os.system("cls")
    print("")
    print("   > MENU   >  Administrador")
    print("")
    print("Bienvenido al administrador donde usted puede configurar los paquetes de viaje")
    print("")
    print("\t[1]   |    Agregar ")
    print("\t[2]   |    Modificar")
    print("\t[3]   |    Eliminar")
    print("\t[4]   |    Visualizar")
    print("\t[5]   |    Salir")
    print("")
    print("")
    while True:
        try:
            opcion=int(input("Ingrese una opcion: "))
            break
        except ValueError:
            print("Opcion incorrecta...")
            administrador()
    if opcion==1:
        agregar()
    elif opcion==2:
        modificar()
    elif opcion==3:
        eliminar()
    elif opcion==4:
        ver()
    elif opcion==5:
        os.system("cls")
        print("El programa se esta cerrando")
        time.sleep(2)
        sys.exit(1)        
    else:
        print("Opcion incorrecta...")
        menu()
def ver():
    os.system("cls")
    con=sqlite3.connect("crucero.s3db")
    cursor=con.cursor()
    cursor.execute("select * from paquetes")
    print("Usted esta viendo las ofertas")
    for v in cursor:
        print("Ruta: ",v[1])
        print("A bordo de: ",v[2])
        print("Clase: ",v[3])
        print("Duracion: ",v[4]," dias con ",v[5]," noches")
        print("Puerto de Salida: ",v[6])
        print("Puerto de Llegada: ",v[7])
        print("Fecha de Salida: ",v[8])
        print("Fecha de Llegada: ",v[9])
        print("Precio: $",v[10])
        print("\n----------------------------\n")
    con.commit()
    con.close()
    input("¡Disfruta de un tour en tierra mientras viajas en crucero..!")
    menu()
def agregar():
    os.system("cls")
    ruta=input("Ruta:  ")
    barco=input("A bordo de: ")
    clase=input("Clase: ")
    dias=input("Dias: ")
    noches=input("Noches: ")
    puertosalida=input("Puerto de Salida: ")
    puertollegada=input("Puerto de Llegada: ")
    fechasalida=input("Fecha de Salida: ")
    fechallegada=input("Fecha de Llegada: ")
    precio=input("Precio: $")
    con=sqlite3.connect("crucero.s3db")
    cursor=con.cursor()
    cursor.execute("insert into paquetes (ruta, barco, clase, dias, noches, puertosalida, puertollegada, fechasalida, fechallegada, precio) values ('"+ruta+"','"+barco+"','"+clase+"','"+dias+"','"+noches+"','"+puertosalida+"','"+puertollegada+"','"+fechasalida+"','"+fechallegada+"','"+precio+"')")
    con.commit()
    con.close()
    os.system("cls")
    input("¡Paquete de viaje registrado con exito..!")
    menu()
def modificar():
    os.system("cls")
    con=sqlite3.connect("crucero.s3db")
    cursor=con.cursor()
    cursor.execute("select * from paquetes")
    print("Usted esta viendo las ofertas")
    for v in cursor:
        print("Ruta: ",v[1])
        print("A bordo de: ",v[2])
        print("Clase: ",v[3])
        print("Duracion: ",v[4]," dias con ",v[5]," noches")
        print("Puerto de Salida: ",v[6])
        print("Puerto de Llegada: ",v[7])
        print("Fecha de Salida: ",v[8])
        print("Fecha de Llegada: ",v[9])
        print("Precio: $",v[10])
        print("\n----------------------------\n")
    codigo=input("Digite el codigo del paquete que desea modificar: ")    
    print("\nIngrese los datos del paquete a modificar:\n")
    ruta=input("Ruta:  ")
    barco=input("A bordo de: ")
    clase=input("Clase: ")
    dias=input("Dias: ")
    noches=input("Noches: ")
    puertosalida=input("Puerto de Salida: ")
    puertollegada=input("Puerto de Llegada: ")
    fechasalida=input("Fecha de Salida: ")
    fechallegada=input("Fecha de Llegada: ")
    precio=input("Precio: $")
    cursor.execute("update paquetes set ruta='"+ruta+"',barco='"+barco+"',clase='"+clase+"',dias='"+dias+"',noches='"+noches+"',puertosalida='"+puertosalida+"',puertollegada='"+puertollegada+"',fechasalida='"+fechasalida+"',fechallegada='"+fechallegada+"',precio='"+precio+"' where ID='"+codigo+"'")
    con.commit()
    con.close()
    os.system("cls")
    input("¡Paquete de viaje modificado con exito..!")
    menu()
def eliminar():
    os.system("cls")
    con=sqlite3.connect("crucero.s3db")
    cursor=con.cursor()
    cursor.execute("select * from paquetes")
    print("Usted esta viendo las ofertas")
    for v in cursor:
        print("Ruta: ",v[1])
        print("A bordo de: ",v[2])
        print("Clase: ",v[3])
        print("Duracion: ",v[4]," dias con ",v[5]," noches")
        print("Puerto de Salida: ",v[6])
        print("Puerto de Llegada: ",v[7])
        print("Fecha de Salida: ",v[8])
        print("Fecha de Llegada: ",v[9])
        print("Precio: $",v[10])
        print("\n----------------------------\n")
    codigo=input("Digite el codigo del paquete que desea eliminar: ")
    cursor.execute("delete from paquetes where ID='"+codigo+"'")
    con.commit()
    con.close()
    os.system("cls")
    input("¡Paquete de viaje eliminado con exito..!")
    menu() 
menu()
        


