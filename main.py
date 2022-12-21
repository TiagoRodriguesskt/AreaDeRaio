'''Faça um algoritmo para calcular a área de uma circunferência, considerando a
 formula ÁREA = π * RAIO2
 . Utilize as variáveis AREA e RAIO, a constante π (pi =
 3,14159) e os operadores aritméticos de multiplicação'''

# Algoritmo simples em Python que calcula a área de um círculo

import math

def calc_area(radius):
    # calculado a area de um circulo
    area = math.pi * radius ** 2
    return area


# Teste a função com um raio de 5
radius = 5
result = calc_area(radius)
print(result)

'''Isso imprimirá a área de um círculo com um raio de 5. O valor de pié importado do mathmódulo, 
que fornece funções matemáticas e constantes. O **operador é usado para calcular o quadrado do raio.'''


#  Você também pode definir o valor de picomo uma constante em seu código, assim
def calc_area(radius):
    # Defina o valor de pi como uma constante
    PI = 3.14159
    # Calcule a área do círculo
    area = PI * radius ** 2
    return area
