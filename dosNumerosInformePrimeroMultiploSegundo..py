#Realizar un programa en el cual se ingresen dos numeros e informe si el primero es múltiplo del segundo.
#En caso contrario deberá generar un mensaje adecuado.
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num1 = int(num1)
num2 = int(num2)
if (num1%num2) == 0:
    print(f"El primer número si es múltíplo del segundo.")
elif (num1%num2) != 0:
   print(f"No son múltiplos") 
else: 
    print("Error, intente de nuevo.")