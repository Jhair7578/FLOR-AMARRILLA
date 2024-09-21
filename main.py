from turtle import *
import colorsys
import math

# Ocultar la tortuga antes de empezar
hideturtle()

# Agregar el texto en la cabecera centrado y con mejor diseño
header_text = "FELIZ 21 DE SEPTIEMBRE 🌻"
color("white")  # Color del texto
penup()  # Levantar el lápiz para evitar dibujar una línea
goto(0, 250)  # Posicionar el texto en el centro (en X) en la parte superior
pendown()  # Bajar el lápiz para escribir el texto
write(header_text, align="center", font=("Arial", 24, "bold"))  # Texto centrado, más grande y en negrita

# Levantar el lápiz nuevamente antes de mover a la posición de los pétalos
penup()
goto(0, -40)  # Moverse a la posición inicial de los pétalos
pendown()  # Bajar el lápiz para empezar a dibujar los pétalos

speed(0.25)
bgcolor("black")

# Mostrar la tortuga para dibujar los pétalos y el centro
showturtle()

# Generar los pétalos
h = 0
for i in range(16):
    for j in range(18):
        c = colorsys.hsv_to_rgb(0.125 , 1, 1)
        color(c)
        rt(90)
        circle(150 - j * 6, 90)
        lt(90)
        circle(150 - j * 6, 90)
        rt(180)
    circle(40, 24)

# Generar la parte central de la flor
color("black")
shape("turtle")
fillcolor("brown")
phi = 137.508 * (math.pi / 180.0)

for i in range(200):
    r = 4 * math.sqrt(i)
    theta = i * phi
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    penup()
    goto(x, y)
    setheading(i * 137.508)
    pendown()
    stamp()

# Ocultar la tortuga antes de escribir el texto debajo del girasol
hideturtle()

# Agregar el texto debajo del girasol centrado y con mejor diseño
penup()
goto(0, -300)  # Posicionar el texto en el centro (en X) debajo del girasol
pendown()
color("white")  # Color del texto
footer_text = "Que este día esté lleno de alegría y colores!"
write(footer_text, align="center", font=("Arial", 16, "italic"))  # Texto centrado, en cursiva y con tamaño moderado

done()
