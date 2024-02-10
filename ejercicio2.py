#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
def check_password(passw,verif):
        
            try:
               
                if passw==verif:
                    print("The password is correct you have access.")
                 
            except:
                 print("The password is not correct .")


if __name__ == "__main__":
    enter_password=(input("Enter the password,please:"))
    verif=(input("Enter the password again,please:"))
    check_password(enter_password,verif)
#funciona