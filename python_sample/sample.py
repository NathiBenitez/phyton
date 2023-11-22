def imprimir_resultados():
    print( 'Resultados hasta la fecha.' )
    read_file = open("data.txt", "r")
    print( read_file.read() )
    read_file.close()       

def ingresar_comentarios():
    while True:
        print( 'Seleccione el proceso que desea aplicar' )
    print( '1:Introducir puntos de evaluación y comentarios' )
    print( '2:Comprueba los resultados hasta ahora.' )
    print( '3:Salir.' )
    num = input()

    if num.isdecimal():
        num = int(num)
        if num == 1:
            print( 'Por favor, introduzca una puntuación en una escala de 1 a 5' )
            point = input()
            if point.isdecimal():
                  point = int(point)
                  if  point <= 0 or point > 5: # Expresión condicional de menor que 0 o mayor que 5.
                      print( 'Indíquelo en una escala de 1 a 5' )
                      point = input()
                  else:
                      print( 'Introduzca sus comentarios.' )
                      comment = input()
                      post = f'punto: {point} comentario: {comment}'
                      file_pc = open("data.txt", 'a')
                      file_pc.write( f'{ post } \n' )
                      file_pc.close()
            else:  
                print( 'Indíquelo en una escala de 1 a 5' )
        elif num == 2:
          print( 'Resultados hasta la fecha.' )
          read_file = open("data.txt", "r")
          print( read_file.read() )
          read_file.close()
        elif num == 3:
          print( 'Terminación.' )
          
        else:
            print( 'Introduzca de 1 a 3' )
    else:
        print( 'Introduzca de 1 a 3' )