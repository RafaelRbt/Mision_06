#Rafael Romero Bello A01747730 Este programa crea figuras.
import math
import pygame
import random

def color():
    color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    return random.choice(color)

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)
VERDE_BANDERA = (27, 94, 32)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)


# Estructura básica de un programa que usa pygame para dibujar
def dibujar(r, R, l):
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True  # Queremos terminar el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)

        radio = 100
        for angulo in range(0, 360 + 1, 20):
            a = math.radians(angulo)  # Convierte a radianes
            x = int(radio * math.cos(a))
            y = int(radio * math.sin(a))
            pygame.draw.circle(ventana, color(), ((x + ALTO // 2), (ANCHO // 2 + y)), radio, 1)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps
    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    r = eval(input("valor de r:"))
    R = eval(input("valor de R: "))
    l = eval(input("valor de l: "))
    dibujar(r, R, l)


# Llamas a la función principal
main()