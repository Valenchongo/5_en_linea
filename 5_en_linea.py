from math import floor
import gamelib

ANCHO_VENTANA = 300
ALTO_VENTANA = 300
DIMENSION = 10
X = "X"
O = "O"

def juego_crear():
    """Inicializar el estado del juego"""
    grilla =[]
    for i in range(0,DIMENSION):
        grilla.append(["" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ])
    return grilla  

def turno (juego):
    """esta funcion sirve para saber si hay mas O o X en la partida para poder saber de quien sera el proximo turno, como se comienza con la X si hay mas X que O en la grilla quiere decir que es el turno de O"""

    contador_x=0
    contador_o=0
    for i in range (0,DIMENSION):
        for c in range (0,DIMENSION):
            if juego[i][c] == X:
                contador_x = contador_x + 1
            elif juego[i][c] == O:
                contador_o = contador_o +1

    if (contador_x > contador_o):
        turno = O
    else:
        turno = X    
    return turno      

def juego_actualizar(juego, x, y):
    #divido la x en 30 y luego uso el metodo floor para hacer el pasaje de pixeles a los numeros que tiene la grilla del juego, a la y le resto 30 ya que la parte donde se puede jugar al juego tiene un margen de 30 pixeles en la parte superior

    if (y<30 or y>330): #si el click esta fuera de las coordenadas dentro del mapa te retorna el juego tal como estaba antes
       return juego

    x , y = x//30 , (y-30)//30
    turn = turno(juego)         
    if ( juego[y][x]== "" ):
        juego[y][x]= turn
    return juego     

def juego_mostrar(juego):
   y_linea = 60
   x_linea = 30
   gamelib.draw_rectangle(0, ALTO_VENTANA // DIMENSION, ANCHO_VENTANA, ALTO_VENTANA+30, outline='white', fill='black')
   gamelib.draw_text('5 en línea', 150, 20)
   turn = turno(juego)
   gamelib.draw_text(f'Turno de : {turn}', 150, 360)
  
   for i in range(0,9):
     y_linea =  (i + 2) * 30
     x_linea = (i + 1) * 30
     gamelib.draw_line(0, y_linea, ANCHO_VENTANA,  y_linea, fill='white', width=1)
     gamelib.draw_line(x_linea, ANCHO_VENTANA // DIMENSION,x_linea,330, fill='white', width=1)
  
   y_jugador = 45    #posicion de la marca en juego[0]
   for i in range (0,DIMENSION):
        x_jugador = 15    #posicion de la marca en juego[0][0]
        for c in range (0,DIMENSION):
            if juego[i][c] == X:
                gamelib.draw_text(X, x_jugador, y_jugador)
 
            elif juego[i][c] == O:
                gamelib.draw_text(O, x_jugador, y_jugador)

            x_jugador = x_jugador+30       
  
        y_jugador = y_jugador+30     
         
def main():
    juego = juego_crear()

    # Ajustar el tamaño de la ventana
    gamelib.resize(ANCHO_VENTANA, ALTO_VENTANA+100)

    # Mientras la ventana esté abierta:
    while gamelib.is_alive():
        # Todas las instrucciones que dibujen algo en la pantalla deben ir
        # entre `draw_begin()` y `draw_end()`:
        gamelib.draw_begin()
        juego_mostrar(juego)
        gamelib.draw_end()

        # Terminamos de dibujar la ventana, ahora procesamos los eventos (si el
        # usuario presionó una tecla o un botón del mouse, etc).

        # Esperamos hasta que ocurra un evento
        ev = gamelib.wait()

        if not ev:
            # El usuario cerró la ventana.
            break

        if ev.type == gamelib.EventType.KeyPress and ev.key == 'Escape':
            # El usuario presionó la tecla Escape, cerrar la aplicación.
            break

        if ev.type == gamelib.EventType.ButtonPress:
            # El usuario presionó un botón del mouse
            x, y = ev.x, ev.y # averiguamos la posición donde se hizo click
            juego = juego_actualizar(juego, x, y)

gamelib.init(main)


