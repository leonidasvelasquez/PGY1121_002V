import os

acumulador_curanto = 0
acumulador_mariscal = 0
acumulador_chupe_centolla = 0
acumulador_empanada = 0

acumulador_pisco_sour = 0
acumulador_bebida = 0
acumulador_jugos = 0

menu = True
menu_p = True
menu_b = True

opcion_general = 0
opcion_platos = 0
opcion_bebidas = 0
continuar = 0

def menu_general():
    os.system("cls")
    print("-- Bienvenido al Restaurante --")
    print("1.- Platos")
    print("2.- Bebidas")
    print("3.- Imprimir boleta")
    print("4.- Salir")
    try:
        opcion_general = int(input("Ingrese una de las opciones del menu general solicitadas > "))
        if opcion_general > 0 and opcion_general < 5:
            return opcion_general
        print("Error al elegir opción en menú general")
    except:
        print("Error al elegir opción en menú general")


def menu_platos():
    # os.system("cls")
    print("-- Menú de platos --")
    print("1.- Curanto              $20.000")
    print("2.- Mariscal             $12.000")
    print("3.- Chupe Centolla       $15.000")
    print("4.- Empanada             $3.000")
    try:
        opcion_platos = int(input("Ingrese una de las opciones del menu platos solicitadas > "))
        if opcion_platos > 0 and opcion_platos < 5:
            return opcion_platos
        print("Error al elegir opción en menú de platos")
    except:
        print("Error al elegir opción en menú de platos")

def menu_bebidas():
    # os.system("cls")
    print("-- Menú de bebidas --")
    print("1.- Pisco Sour        $5.000")
    print("2.- Bebida Lata       $3.000")
    print("3.- Jugo              $2.000")
    try:
        opcion_bebidas = int(input("Ingrese una de las opciones del menu de bebidas solicitadas > "))
        if opcion_bebidas > 0 and opcion_bebidas < 4:
            return opcion_bebidas
        print("Error al elegir opción en menú bebidas")
    except:
        print("Error al elegir opción en menú bebidas")

def imprimir_boleta():
    # os.system("cls")
    print("____ BOLETA _____")
    input("")

def continuar_comprando():
    try:
        continuar = int(input("Desea seguir comprando? 1=SI 2=NO > "))
        if continuar == 1:
            return True
        else:
            return False
    except:
        print("Error al coninuar")




while menu:
    valor_general = menu_general() 
    if valor_general == 1:

        menu_p = True
        while menu_p:
            valor_platos = menu_platos()
            if valor_platos == 1:
                acumulador_curanto += int(input("Cuantos curantos desea comprar > "))
                menu_p = continuar_comprando()
                opcion_platos = 0

            if valor_platos == 2:
                acumulador_mariscal += int(input("Cuantos Mariscales desea comprar > "))
                menu_p = continuar_comprando()
                opcion_platos = 0

            if valor_platos == 3:
                acumulador_chupe_centolla += int(input("Cuantos Chupe centolla desea comprar > "))
                menu_p = continuar_comprando()
                opcion_platos = 0

            if valor_platos == 4:
                acumulador_empanada += int(input("Cuantas empanadas desea comprar > "))
                menu_p = continuar_comprando()
                opcion_platos = 0

        
        input("salió del while platos")

            



    if valor_general == 2:

        menu_b = True
        while menu_b:
            if menu_bebidas() == 1:
                acumulador_pisco_sour += int(input("Cuantos Pisco SOur desea comprar > "))
            if menu_bebidas() == 2:
                acumulador_bebida += int(input("Cuantas Bebidas desea comprar > "))
            if menu_bebidas() == 3:
                acumulador_jugos += int(input("Cuantos Jugos desea comprar > "))
        
    if valor_general == 3:
        imprimir_boleta()
    if valor_general == 4:
        menu = False


os.system("cls")
print("Salió del sistema")