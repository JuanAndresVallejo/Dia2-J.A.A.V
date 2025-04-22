numero1 = float(input("Escribe un numero "))
numero2 = float(input("Ahora otro numero "))
numero3 = float(input("Por ultimo, el tercer numero "))
if (numero1 < numero2 and numero1 < numero3):
    print(f"{numero1:.2f} es el menor!")
elif (numero2 < numero1 and numero2 < numero3):
    print(f"{numero2:.2f} es menor!")
else:
    print(f"{numero3:.2f} es menor!")