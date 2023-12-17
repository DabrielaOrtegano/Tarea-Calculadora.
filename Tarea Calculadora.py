print("Calculadora en operación")
i=1
while i==1 :
    numero1=int(input("Ingrese el primer número (recuerde entre 40 y 200): "))
    while numero1<40 or numero1>200 :
        numero1=int(input("Número incorrecto, (recuerde entre 40 y 200): "))
    numero2=int(input("Ingrese el segundo número (entre 40 y 200): "))
    while numero2<40 or numero2>200 :
        numero2=int(input("Número incorrecto, (recuerde entre 40 y 200): "))
    print("Escoja una opción")
    print("Para sumar ingrese: 1")
    print("Para restar ingrese: 2")
    print("Para multiplicar ingrese: 3")
    print("Para dividir ingrese: 4")
    print(" ")
    j=int(input())
    while j<1 or j>4 :
        print("Escogió la opción incorrecta, vuelva a intentarlo.")
        j=int (input())
    if j==1 :
        suma=numero1+numero2
        print("La suma es: ",suma)
    elif j==2 :
        resta=numero1-numero2
        print("La resta de n1-n2 es: ",resta)
    elif j==3 :
        producto=numero1*numero2
        print("El producto es: ",producto)
    elif j==4 :
        cociente=numero1/numero2
        print("La división de n1/n2 es: ",cociente)
    print("¿Desea seguir? Sí <1> , No <0>")
    i=input()
    