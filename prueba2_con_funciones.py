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
    os.system("clear")
    print("-- Bienvenido al Restaurante --")
    print("1.- Platos")
    print("2.- Bebidas")
    print("3.- Imprimir boleta")
    print("4.- Salir")
    try:
        opcion = int(input("Ingrese una de las opciones del menu general solicitadas > "))
        if opcion > 0 and opcion < 5:
            return opcion
        print("Error al elegir opción en menú general")
    except:
        print("Error al elegir opción en menú general")

def menu_platos():
    os.system("clear")
    print("-- Menú de platos --")
    print("1.- Curanto              $20.000")
    print("2.- Mariscal             $12.000")
    print("3.- Chupe Centolla       $15.000")
    print("4.- Empanada             $3.000")
    try:
        opcion = int(input("Ingrese una de las opciones del menu platos solicitadas > "))
        if opcion > 0 and opcion < 5:
            return opcion
        print("Error al elegir opción en menú de platos")
    except:
        print("Error al elegir opción en menú de platos")

def menu_bebidas():
    os.system("clear")
    print("-- Menú de bebidas --")
    print("1.- Pisco Sour        $5.000")
    print("2.- Bebida Lata       $3.000")
    print("3.- Jugo              $2.000")
    try:
        opcion = int(input("Ingrese una de las opciones del menu de bebidas solicitadas > "))
        if opcion > 0 and opcion < 4:
            return opcion
        print("Error al elegir opción en menú bebidas")
    except:
        print("Error al elegir opción en menú bebidas")

def imprimir_boleta():
    os.system("clear")
    print("_________ BOLETA _________\n")
    
    if acumulador_curanto > 0:
        print(f"{acumulador_curanto} \t CURANTOS \t\t ${acumulador_curanto*20000}")
    if acumulador_mariscal > 0:
        print(f"{acumulador_mariscal} \t MARISCAL \t\t ${acumulador_mariscal*12000}")
    if acumulador_chupe_centolla > 0:
        print(f"{acumulador_chupe_centolla} \t CHUPE CENTOLLA \t ${acumulador_chupe_centolla*12000}")
    if acumulador_empanada > 0:
        print(f"{acumulador_empanada} \t EMPANADA \t\t ${acumulador_empanada*3000}")
    if acumulador_pisco_sour > 0:
        print(f"{acumulador_pisco_sour} \t PISO sour \t\t ${acumulador_pisco_sour*5000}")
    if acumulador_bebida > 0:
        print(f"{acumulador_bebida} \t BEBIDAS LATA \t\t ${acumulador_bebida*3000}")
    if acumulador_jugos > 0:
        print(f"{acumulador_jugos} \t JUGO \t\t\t ${acumulador_jugos*2000}")
    print("__________________________")
    subtotal = acumulador_curanto*20000 + acumulador_mariscal*12000 + acumulador_chupe_centolla*12000 + acumulador_empanada*3000 + acumulador_pisco_sour*5000 + acumulador_bebida*3000 + acumulador_jugos*2000
    
    print(f"SUBTOTAL \t\t\t {subtotal}")
    descuento = 0
    if subtotal > 50000:
        descuento = subtotal*0.1
    print(f"DESCUENTO \t\t\t {descuento}")
    print("__________________________")
    print(f"TOTAL \t\t\t {subtotal-descuento}")
    print("_ GRACIAS POR SU COMPRA __\n\n")

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
    opcion_general = menu_general()
    if opcion_general == 1:
        
        menu_p = True
        while menu_p:
            opcion_platos = menu_platos()
            if opcion_platos == 1:
                acumulador_curanto += int(input("Cuantos curantos desea comprar > "))
            if opcion_platos == 2:
                acumulador_mariscal += int(input("Cuantos Mariscales desea comprar > "))
            if opcion_platos == 3:
                acumulador_chupe_centolla += int(input("Cuantos Chupe centolla desea comprar > "))
            if opcion_platos == 4:
                acumulador_empanada += int(input("Cuantas Empanadas desea comprar > "))
            
            menu_p = continuar_comprando()

    if opcion_general == 2:

        menu_b = True
        while menu_b:
            opcion_bebidas = menu_bebidas()
            if opcion_bebidas == 1:
                acumulador_pisco_sour += int(input("Cuantos Pisco SOur desea comprar > "))
            if opcion_bebidas == 2:
                acumulador_bebida += int(input("Cuantas Bebidas desea comprar > "))
            if opcion_bebidas == 3:
                acumulador_jugos += int(input("Cuantos Jugos desea comprar > "))
            
            menu_b = continuar_comprando()
        
    if opcion_general == 3:
        imprimir_boleta()
        menu = continuar_comprando()
    if opcion_general == 4:
        menu = False


os.system("clear")
print("Salió del sistema")
