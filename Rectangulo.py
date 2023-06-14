def main():
    """
    Programa que lea los valores (x1, x2, y1, y2) de dos rectángulos e 
    indique si uno de los dos rectángulos se encuentra dentro del otro, si son iguales o 
    si ninguno de los dos está dentro del otro.
    Entradas y restricciones:
    - x1, x2, y1, y2 : Valores de ambos rectángulos, reales no negativos.
    Salidas:
    - Indicar si el primer rectángulo está dentro del segundo, si el segundo está dentro 
    del primero, si los dos son iguales, o si ninguno de los dos está dentro del otro.
    """
    
#Solicitud de valores rectángulo 1:
    
    print("Indique los valores del primer rectángulo: ")
    rec1_x1 = float(input("x1: "))
    rec1_x2 = float(input("x2: "))
    if rec1_x1 > rec1_x2:
        print("El rectángulo no es válido. ")
        input()
        return
    
    rec1_y1 = float(input("y1: "))
    rec1_y2 = float(input("y2: "))
    if rec1_y1 > rec1_y2:
        print("El rectángulo no es válido. ")
        input()
        return
    
#Solicitud de valores rectángulo 2:
        
    print("Indique los valores del segundo rectángulo: ")
    rec2_x1 = float(input("x1: "))
    rec2_x2 = float(input("x2: "))
    if rec2_x1 > rec2_x2:
        print("El rectángulo no es válido. ")
        input()
        return
    
    rec2_y1 = float(input("y1: "))
    rec2_y2 = float(input("y2: "))
    if rec2_y1 > rec2_y2:
        print("El rectángulo no es válido. ")
        input()
        return
    
#Cálculo igualdad de rectángulos:

    if rec1_x1 == rec2_x1 and rec1_x2 == rec2_x2 and rec1_y1 == rec2_y1 and rec1_y2 == rec2_y2:
        print("Los dos rectángulos son iguales.")

#Cálculo segundo dentro del primero:

    elif rec1_x1 <= rec2_x1 and rec1_x2 >= rec2_x2 and rec1_y1 < rec2_y1 and rec1_y2 > rec2_y2:
        print("El segundo rectángulo está dentro del primer rectángulo. ")
    elif rec1_x1 < rec2_x1 and rec1_x2 > rec2_x2 and rec1_y1 <= rec2_y1 and rec1_y2 >= rec2_y2:
        print("El segundo rectángulo está dentro del primer rectángulo. ")

#Cálculo primero dentro del segundo:

    elif rec2_x1 <= rec1_x1 and rec2_x2 >= rec1_x2 and rec2_y1 < rec1_y1 and rec2_y2 > rec1_y2:
        print("El primer rectángulo está dentro del segundo rectángulo. ")
    elif rec2_x1 < rec1_x1 and rec2_x2 > rec1_x2 and rec2_y1 <= rec1_y1 and rec2_y2 >= rec1_y2:
        print("El primer rectángulo está dentro del segundo rectángulo. ")

#Cálculo ninguno dentro del otro:

    elif rec1_x1 < rec2_x1 and rec1_x2 < rec2_x2 or rec1_x1 > rec2_x1 and rec1_x2 > rec2_x2:
        print("Ningún rectángulo está dentro del otro. ")
    elif rec1_y1 < rec2_y1 and rec1_y2 < rec2_y2 or rec1_y1 > rec2_y1 and rec1_y2 > rec2_y2:
        print("Ningún rectángulo está dentro del otro. ")
    input()
main()
