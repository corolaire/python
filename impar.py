def impar(n):
    lista_impar = []
    if n > 0 and type(n) == int:
        for i in range(1, n+1, 2):
            lista_impar.append(i)
        return lista_impar
    else:
        print("Enter a valid positive integer.")

if __name__ == "__main__":
    enter_number = int(input("Enter a number: "))
    result = impar(enter_number)
    
    if result:
        print("Odd numbers from 1 to", enter_number, "are:", ", ".join(map(str, result)))
