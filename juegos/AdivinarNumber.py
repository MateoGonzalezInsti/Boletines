#adivina un numero aleatorio calculado por el pc con base de datos de jugadores. Acierta el numero sib morir y lo más rapido posible
from os import system,path
import random
#funciones
def getDatos():
    #Comentario de la profe: los path de Windows llevan la barra a la inversa \
    if path.exists('juegos\BaseDatos.txt'):
        with  open('juegos\BaseDatos.txt','r') as file:
            datos=""
            for line in file:
                datos+=line
            print('datos:',datos)
            #transformar datos
            #Comentario de la profe: estás intentando utilizar un array multidimensional, que no está bien transformado. Te recomiendo dividir los jugadores por saltos de carro sin usar los corchetes.
            datostransformados=datos.replace("[", "")
            datostransformadosarray=datostransformados.split(']')
            datostransformadosarraymulti = []
            for element in datostransformadosarray:
                if element != '':
                    datostransformadosarraymulti.append(element.split(","))
            return datostransformadosarraymulti
    else :
        setdatos('')

def setdatos(datos):
    with open("juegos\BaseDatos.txt","w") as file:
        file.write(str(datos))
    
def getNumero(vidas,numAdivinar,intentos):#recibir numero usuario y comprobar resultado
    #interfad
    print(f'Vidas restantes {vidas}')
    numeroUsuario=int(input('    Escribe un numero:'))
    #comprobar numero
    if numAdivinar==numeroUsuario:#acierto
        print('¡Lo has acertado!')
    else:#fallo
        vidas-=1
        print('¡Has fallado!')
    intentos+=1
    return [vidas,intentos]
def SumarPuntos(intentos):
    puntosSumar=int(0)
    if ((15-intentos)*5)<5:
        puntosSumar=int(5)
    else:
        puntosSumar=int((15-intentos)*5)
        datosJugadores[puertoJugador][1]+=puntosSumar
def listaJugadores(lista):
    print('Lista de jugadores:')
    #Comentario de la profe: necesitas comprobar contra None en Python sino da error
    if lista!=None and len(lista)!=0:
       #Comentario profe: estás recorriendo una matriz de manera incorrecta
        i = 0
        for element in lista:
            print(f'    {i+1}º->Nombre:{element[0]},Puntuación:{element[1]},Vidas:{element[2]}')
            i = i+1
    else:
        print(' Ninguna partida guardada')
        setdatos("")
terminarPrograma=False
IniciadoPrograma=False
datosJugadores=getDatos()#0:nombre,1:puntuacion,2:vidas
if datosJugadores=='':
    datosJugadores=[]
while terminarPrograma==False:#salir del programa?
    system("cls")
    #cerrar programa?
    if IniciadoPrograma==False:
        IniciadoPrograma=True
    else:
        cerrarPrograma=str(input('Quieres cerrar el programa? (y/n)'))
        if IniciadoPrograma==True and cerrarPrograma=='y':
            terminarPrograma=True
            break
    #iniciar jugador 
    print('Juego de adivinar un numero')
    listaJugadores(datosJugadores)
    print('Creando jugador...')
    nombreUsuario=str(input('   Escriba su nombre:'))
    puertoJugador=int(-1)#importante(indice del array para acceder a los datos de guardado)
    for i in range(len(datosJugadores)):#encontrar si existen datos de guardado
        if datosJugadores[i][0]==nombreUsuario:
            puertoJugador=i
    valoresDefectoCuenta=[nombreUsuario,0,6]
    if puertoJugador==-1:#no se encontro datos guardados
        puertoJugador=len(datosJugadores)
        #guardar datos si no existen
        datosJugadores.append(valoresDefectoCuenta)#valores por defecto
    else:#existen
        #comprobar si tiene vidas
        if datosJugadores[puertoJugador][2]<=0:#no tiene vidas
            #reiniciar datos del jugador
            datosJugadores[puertoJugador]=valoresDefectoCuenta#valores por defecto
    setdatos(datosJugadores)
    #generar partidas
    terminarGenerarPartidas=False
    primeraPartida=False
    while terminarGenerarPartidas==False and datosJugadores[puertoJugador][2]>0:#bucle partidas
        #continuar
        if primeraPartida==False:
            system("cls")
            primeraPartida=True
        else:
            setdatos(datosJugadores)
            salir=str(input('Quieres salir? (y/n)'))
            if salir=='y':
                terminarGenerarPartidas=True
                break
        #numero random
        numeroRangoUsuario=int(input('Escribe el rango de numeros posibles: 1...'))
        numeroAdivinar=random.randint(1,numeroRangoUsuario)
        system("cls")
        print('¡Recuerda la partida se termina cuando se te acaben las vidas o abandones!')
        #datos partida
        partidaGanada=False
        intentosPartida=int(0)
        terminarPartida=False
        while terminarPartida==False and datosJugadores[puertoJugador][2]>0:
            vidasJugadoractual=datosJugadores[puertoJugador][2]
            getDatos=getNumero(datosJugadores[puertoJugador][2],numeroAdivinar,intentosPartida)
            intentosPartida=getDatos[1]
            datosJugadores[puertoJugador][2]=getDatos[0]
            if vidasJugadoractual==datosJugadores[puertoJugador][2]:#acertado
               terminarPartida=True
               partidaGanada=True
            if datosJugadores[puertoJugador][2]<=0:
                terminarPartida=True
                partidaGanada=False
        #sumar una vida si gano la partida
        if partidaGanada==True:
            datosJugadores[puertoJugador][2]+=int(1)
            print(f'Partida acabada. Intentos:{intentosPartida}, Vidas:{datosJugadores[puertoJugador][2]}')
        
system("cls")
print('Programa finalizado...')
