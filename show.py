#Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
def show(data):
    while data!="stop":
        try:
            data=(input("Enter a word:"))
            a=lista_string.append(data)
            print(lista_string)
            data=(input("Enter the next word:"))
    


        except:
            print("The data enter is not correct.")
        




if __name__=="__main__":
    enter_string=(input("Enter the world:"))
    lista_string=[]
    show(lista_string)